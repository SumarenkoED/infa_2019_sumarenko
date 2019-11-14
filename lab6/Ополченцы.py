from tkinter import *
from random import randrange as rnd, choice
import time
import math


start_time = time.time()
#print("--- %s seconds ---" % (time.time() - start_time))
root = Tk()
updateTime = 30
balls = []
Rectangles = []
c = Canvas(root, width = 960, height = 760, bg = 'white')
c.pack()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
ptr = 1
LVL = 1
k = 0
tim = 0
koeff = 1


class Ball:
    global koeff
    
    def __init__(self):
        self.x = rnd(60, 700)
        self.y = rnd(60, 700)
        self.Vx = rnd (-7 * koeff, 7 * koeff)
        self.Vy = rnd (-7 * koeff, 7 * koeff)
        self.r = rnd (30, 50)
        self.id = c.create_oval(self.x - self.r, self.y - self.r, 
                                self.x + self.r, self.y + self.r, 
                                fill = choice(colors), width = 0
                                )

    def reflection_ball(self):
        if self.y <= self.r or self.y >= 760 - self.r:
            self.Vy *= -1
        if self.x <= self.r or self.x >= 760 - self.r:
            self.Vx *= -1

    def move_ball(self):
        c.move(self.id, self.Vx, self.Vy)
        self.y += self.Vy
        self.x += self.Vx

    def inside_ball(self, xClick, yClick):
        return ((xClick - self.x) ** 2 + (yClick - self.y) ** 2) ** 0.5 < self.r

    def delete_ball(self):
        self.x = -100
        self.y = -100
        c.delete(self.id)


class Rectangle:
    global koeff, ptr

    def __init__(self):
        self.x = rnd(70, 690)
        self.y = rnd(130, 530)
        self.Vx = rnd (-3 * koeff, 3 * koeff)
        self.Vy = rnd (-3 * koeff, 3 * koeff)
        self.r = rnd (30, 70)
        self.a1 = rnd(50, 100)
        self.w1 = rnd(1 * koeff, 100 * koeff)
        self.w1 = self.w1 / 1000
        self.b1 = rnd(50, 100)
        m = choice(colors)
        self.id = c.create_rectangle(self.x, self.y, self.x + self.r, 
                                     self.y + 2 * self.r, fill = m, 
                                     outline = m, width = 3
                                     )

    def move_rectangle(self):
        c.move(self.id, self.Vx, self.Vy)
        self.Vx = -self.a1 * self.w1 * math.sin(self.w1 * ptr)
        self.Vy = self.b1 * self.w1 * math.cos(self.w1 * ptr)
        self.y += self.Vy
        self.x += self.Vx

    def inside_rectangle(self, xClick, yi):
        return (self.x < xClick) * (self.x + self.r > xClick) * (self.y < yi) * (self.y + 2 * self.r > yi) == 1

    def delete_rectangle(self):
        self.x = -100
        self.y = -100
        c.delete(self.id)


#обновление

def updateScene():
    global ptr
    for b in balls:
        b.move_ball()
        b.reflection_ball()
    for d in Rectangles:
        d.move_rectangle() 
    ptr += 1
    root.after(updateTime, updateScene)

def mouseClick(event):
    global k, LVL, tim, koeff
    for i in range(len(balls)):
        if balls[i].inside_ball(event.x, event.y):
            k += 1
            tim += 1
            balls[i].delete_ball()
        if tim == n + f:
            tim = 0
            LVL += 1
            realise()
            koeff += 1
    for j in range(len(Rectangles)):
        if Rectangles[j].inside_rectangle(event.x, event.y):
            k += 10
            tim += 1
            Rectangles[j].delete_rectangle()
        if tim == n + f:
            tim = 0
            LVL += 1
            realise()
            koeff += 1
    if k >= 10:
        c.delete_rectangle(ALL)
        c.create_text(500, 350, text = str(time.time() - start_time()), 
                      anchor = SE, fill = "black")

def realise():
    global n, f, tim
    f = rnd(0,20)
    n = rnd(0, 50)
    c.bind('<Button-1>', mouseClick)
    for i in range(n):
        balls.append(Ball())
    for i in range(f):
        Rectangles.append(Rectangle())

realise()

#таблицы

c.create_line(4, 4, 4, 757, 757, 757, 757, 4)
c.create_rectangle(955, 5, 763, 95, fill = 'orange', outline = 'orange',
                    width = 3, activedash = (5, 4))
c.create_rectangle(955, 105, 763, 755, fill = 'green', outline = 'green',
width = 3, activedash = (5, 4))
c.create_text(885, 30, text = "Игрок:",
                anchor = SE, fill = "black")
c.create_text(873, 125, text = "Ополчение ДНР:",
anchor = SE, fill = "black")

#авторизация пользователя

e = Entry(root, width = 18)
b = Button(text = "Представиться")
l = Label(bg = 'black', fg = 'white', width = 20)

def strToSortlist(event):
    global name
    name = e.get()
    text_f = open('text.txt', 'a')
    text_f.write(name)
    text_f.write(' ')
    l['text'] = ' '.join(name)

b.bind('<Button-1>', strToSortlist)
e.place(x = 772, y = 35)
b.place(x = 830, y = 65)
for i in range(20):
    c.create_text(780, 145 + i * 20, text = i + 1,
    anchor = SW, fill = "black")
text_f = open('text.txt', 'r')
i = 0
for line in text_f:
    i += 1
    c.create_text(800, 140 + i * 20, text = line, anchor = SW, fill = "black")
root.after(updateTime, updateScene)


mainloop()

#работа с файлом и вывод таблицы лучших игроков на экран

text_f = open('text.txt', 'a')
text_f.write(str(k))
text_f = open('text.txt', 'r')
s = 0
for line in text_f:
    s += 1
text_f = open('text.txt', 'r')
Name = [0] * s
BRS = [0] * s
for i in range (s):
    sesc = text_f.readline().split()
    Name[i] = sesc[0]
    BRS[i] = sesc[1]
for i in range (s):
    BRS[i] = int(BRS[i])
for j in range (s - 1):
    for i in range (s - j - 1):
        if (BRS[i + 1] > BRS[i]):
            BRS[i], BRS[1 + i] = BRS[1 + i], BRS[i]
            Name[i], Name[1 + i] = Name[1 + i], Name[i]
for i in range(s):
    BRS[i] = str(BRS[i])
text_f = open('text.txt', 'w')
for i in range (s):
    text_f.write(Name[i])
    text_f.write(' ')
    text_f.write(BRS[i])
    text_f.write("\n")
text_f.close()


root.mainloop()