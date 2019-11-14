from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import array


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

class ball():
    
    def __init__(self, x=25, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y <=500:
            self.vy-=1.2
            self.x += self.vx
            self.y -= self.vy
            self.vx *= 0.99
            self.set_coords()
        else:
            if self.vx**2+self.vy**2>10:
                self.vx=self.vx/2
                self.vy=-self.vy/2
                self.y=499
            if self.live<0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live-=1
        if self.x>780:
            self.vx=-self.vx/2
            self.x=779

    def hittest(self, obj):
        
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if  abs(obj.x-self.x)<=(self.r+obj.r) and abs(obj.y-self.y)<=(self.r+obj.r):
            return True
        else:
            return False

class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = (math.atan((event.y-new_ball.y) / (event.x-new_ball.x)))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():

    def __init__(self):
        self.points = 0
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = '',font = '28')
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(7, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        self.y += self.vy
        self.x += self.vx
        canv.move(self.id, self.vx, self.vy)
        self.vy += 0.1
        if self.y < 10 + self.r:
            self.y = 10 + self.r
            self.vy = -self.vy
        elif self.y > 550 - self.r:
            self.y = 550 - self.r
            self.vy = -self.vy
        if self.x < 10 + self.r:
            self.x = 10 + self.r
            self.vx = -self.vx
        elif self.x > 750 - self.r:
            self.x = 750 - self.r
            self.vx = -self.vx

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text='')

screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
targets = []


def new_game():
    global gun, screen1, balls, bullet
    canv.itemconfig(screen1, text='')
    bullet = 0
    balls = []
    targets = []
    tlive = 0
    for i in range(2):
        new_target = target()
        targets.append(new_target)
        tlive += targets[i].live
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
 
    while tlive or balls:
        delit = []
        for j in range(2):
            targets[j].move()
        for i, b in enumerate(balls):
            b.move()
            for j in range(2):
                if b.hittest(targets[j]) and targets[j].live:
                    tlive -= targets[j].live
                    targets[j].live = 0
                    targets[j].hit()
            if b.live < 0:
                    delit.append(i)
                    canv.delete(b.id)
            for i in range(len(delit) - 1):
                del balls[delit[i]]
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.bind('<Button-1>', '')
    canv.bind('<ButtonRelease-1>', '')
    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
    canv.delete(gun)
    root.after(1500, new_game)


new_game()

root.mainloop()