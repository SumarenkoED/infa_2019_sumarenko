def branch(x, y, a, c1, c2, color_red, color_green, color_blue):
    """Рисует ветку в виде гиперболы y=kx*x с координатами вершины x,y
    и параметром k=a в промежутке по x от с1 до с2"""
    penSize(1)
    penColor( color_red, color_green, color_blue)
    for i in range (c1,c2):
        c = a * i * i
        x1 = i + x
        y1 = c + y
        point (x1, y1, -1)

def ellipse(x, y, a, b, fi, color_red, color_green, color_blue):
    """Рисует эллипс с координатами центра x и y и длинами горизонтальной оси a и вертикальной b
        и поворачивает его на fi радиан (цвет эллипса (color_red, color_green, color_blue) по RGB)"""
    brushColor(color_red, color_green, color_blue)
    penColor(color_red, color_green, color_blue)
    db = b / 100
    left = []
    right = []
    for i in range(-100, 101):
        y0 = i * db
        x0 = a * abs((1 - (i * db / b) ** 2) ** 0.5)
        left.append([-x0, y0])
        right.append([x0, y0])
    L = len(left)
    for j in range(L):
        left.append(right[L - j - 1])
    for k in range(len(left)):
        x0 = left[k][0]
        y0 = left[k][1]
        x1 = x + x0 * math.cos(fi) + y0 * math.sin(fi)
        y1 = y - x0 * math.sin(fi) + y0 * math.cos(fi)
        left[k][0] = x1
        left[k][1] = y1
    polygon(left)

def tree (x,y,h,l,m,color_red, color_green, color_blue):
    """Рисует дерево с координатами левого верхнего угла нижней части ствола x и y,
    её высотой h, толщиной l, с изгибом веток m и цветом цвет эллипса color_red, color_green, color_blue) по RGB"""
    penSize(1)
    penColor(color_red, color_green, color_blue)
    brushColor(color_red, color_green, color_blue)
    polygon([(x-0.2*h,y-22*l/18),(x+0.4*h, y-21*l/18),(x+h, y-33*l/18),(x+0.35*h, y-34*l/18)])
    polygon([(x+0.4*h,y-36*l/18),(x+0.7*h, y-35.2*l/18),(x+1.63*h, y-49*l/18),(x+1.3*h, y-50*l/18)])
    rectangle(x, y, x+h, y+l)
    rectangle(x, y-0.1*l, x+h, y-1.1*l)
    penSize(1)
    branch (x+4*h, y-26*l/18, 22*m/120000, int(-2.5*h), int(1.2*h), color_red, color_green, color_blue)
    branch (x+8*h, y-50*l/18, 6*m/120000, int(-6.2*h), int(1.2*h), color_red, color_green, color_blue)
    branch (x-2.4*h, y-13*l/18, 19*m/120000, int(-1.2*h), int(2.2*h), color_red, color_green, color_blue)
    branch (x-5.5*h, y-38*l/18, 9*m/120000, int(-0.5*h), int(4.7*h), color_red, color_green, color_blue)
    ellipse (x+3.3*h, y-16*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x+4*h, y-19*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x+4.8*h, y-18*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x+5*h, y-38*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x+5.8*h, y-40*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x+6.6*h, y-42*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x+7.4*h, y-44*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x+8.4*h, y-43.5*l/18, int(h/5), int(l/3), 60, color_red, color_green, color_blue)
    ellipse (x-3.3*h, y-6*l/18, int(h/5), int(l/3), -60, color_red, color_green, color_blue)
    ellipse (x-2.7*h, y-7*l/18, int(h/5), int(l/3), -60, color_red, color_green, color_blue)
    ellipse (x-2.1*h, y-6*l/18, int(h/5), int(l/3), -60, color_red, color_green, color_blue)
    ellipse (x-3.3*h, y-26*l/18, int(h/5), int(l/3), -60,  color_red, color_green, color_blue)
    ellipse (x-3.9*h, y-28*l/18, int(h/5), int(l/3), -60,  color_red, color_green, color_blue)
    ellipse (x-4.7*h, y-31*l/18, int(h/5), int(l/3), -60,  color_red, color_green, color_blue)
    ellipse (x-5.4*h, y-32*l/18, int(h/5), int(l/3), -60,  color_red, color_green, color_blue)
    ellipse (x-6*h, y-32*l/18, int(h/5), int(l/3), -60,  color_red, color_green, color_blue)

def panda(x,y,h,with_branch):
    """Рисует панду с координатами середины тела x и y и высотой тела h,
    которая ест бамбук, если with_branch=1"""
    penColor('black')
    brushColor('black')
    polygon([(x-1.5*h,y),(x-1.3*h,y+1.5*h),(x-1.7*h,y+2*h),(x-2.5*h,y+1.7*h),(x-2.25*h,y+0.3*h)])
    ellipse(x-(2.25*h+2.5*h)/2, y+h, int(h/5), int(5*h/6), -19*3.14/180, 0,0,0)
    ellipse(x-(1.7*h+2.5*h)/2, y+(1.7*h+2*h)/2, int(2*h/3), int(h/5), (-20)*3.14/180, 0,0,0)
    brushColor(200, 130, 105)
    penColor(200, 130, 105)
    polygon([(x-1.3*h,y+1.5*h),(x-2.1*h,y+2.5*h),(x-1.2*h, y+2.1*h)])
    ellipse(x,y,int(2*h),h,0, 255,255,255)					#body
    brushColor('black')
    penColor('black')
    polygon([(x+h/7,y-7*h/6),(x+h/7,y+7*h/6),(x,y+14*h/7),(x-h/2,y+17*h/7),(x-5*h/6,y+10*h/7)])
    brushColor('white')
    penColor('white')
    circle(x-h/8,y+2*h/3-h/8,h/4)
    polygon([(x,y+2*h/3),(x,y-2*h/3),(x-h,y-1.5*h),(x-2*h,y-2*h/3),(x-2*h, y+5*h/6)])
    ellipse(x, y, int(h/4), int(2*h/3), 0, 255,255,255)
    ellipse(x-h/2, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3+h/10), -40, 255, 255, 255)
    ellipse(x-1.5*h, y-(1.5*h+2*h/3)/2, int(h/4), int(2*h/3), 40,  255, 255, 255)
    ellipse(x-2*h, y-(2*h/3-5*h/6)/2, int(h/4), int(2*h/3+h/7), 0,  255, 255, 255)
    ellipse(x-h, y+(5*h/6+2*h/3)/2, int(h/4), int(2*h/3+h/3), -88*3.14/180,  255, 255, 255)
    circle(x-h-h/10, y+h/3-2*h/10, h/3)
    penColor('black')   
    ellipse(x-2*h, y+h/3-1.5*h/5, int(h/4), int(h/3), 0, 0, 0, 0) 			#right eye
    ellipse(x-2*h, y+h/3-1.5*h/5, int(h/7), int(h/8), 0, 255, 255, 255)
    ellipse(x-2*h-h/20, y+h/3-1.5*h/5-h/25, int(h/10), int(h/12), 0, 0, 0, 0)
    if with_branch==1:															#branch
	    branch(x-2*h+h/10+h/5, y+h,0.01,int(-1.2*h), int(1.0*h), 0, 255, 0)
	    ellipse(x-2*h+h/10-h/3, y+h-h/5+h/1.5, int(h/10), int(h/4), 0, 0, 255, 0)
	    ellipse(x-2*h+h/10-h/3-h/4, y+h-h/5+h/1.5, int(h/20), int(h/8), 0, 0, 255, 0)
	    ellipse(x-2*h+h/10-h/3-h/4, y+h-h/5, int(h/10), int(h/4), 3.14/4, 0, 255, 0)
	    ellipse(x-2*h+h/10-h/3-h/2, y+h-h/5+h/4, int(h/20), int(h/8), 3.14/4, 0, 255, 0)
    ellipse(x-2*h+h/10, y+h-h/5, int(h/3), int(h/4), 0, 0,0,0)				#nose
    brushColor('black')
    ellipse(x-(h/2+5*h/6)/2, y+(27*h/7)/2, int(1.2*h/2), int(h/2), 12*3.14/180, 0, 0, 0)
    ellipse(x-2*h+h/10, y-(5*h/6+2*h/3)/2-h/3, int(h/4), int(h/3+h/3), -40*3.14/180, 0, 0, 0)  #right yer
    ellipse(x, y-(5*h/6+2*h/3)/2-h/15, int(h/4), int(h/3+h/3), 30*3.14/180, 0, 0, 0)			#left yer
    circle(x-1.1*h,y+0.25*h,h/4)
    ellipse(x-1.1*h,y+0.25*h, int(h/7), int(h/8), 0, 255,255,255)
    ellipse(x-1.1*h-h/20,y+0.25*h-h/25, int(h/10), int(h/12), 0, 0, 0, 0)					#left eye
    ellipse(x+1.2*h,y+1.3*h,int(1.3*h),int(0.6*h), 60*3.14/180, 0, 0, 0)					#back paw
    ellipse(x+1.2*h-0.6*h,y+1.3*h+0.6*h,int(0.5*h),int(0.6*h), 0, 0, 0, 0)


from graph import *
import math


windowSize(600, 400)
canvasSize(600, 400)
width, height = windowSize()
brushColor(200, 130, 105)
rectangle(0,0, 600,400)
brushColor(250, 250, 105)
penColor(250, 250, 105)
circle(155,150,70)
tree (270, 200, 20, 70, 100,30, 200, 30)
tree (170, 230, 8, 50, 200, 60, 225, 4)
tree (70, 225, 12, 50, 250, 20, 180, 80)
tree (510, 200, 9, 60, 300, 50, 190, 60)
brushColor('white')
penColor('white')
panda(400, 250, 40, 1)
panda(230, 330, 20, 0)
penColor('black')

run()
