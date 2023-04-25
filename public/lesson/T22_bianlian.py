import turtle
turtle.tracer(False)
turtle.mode('logo')
turtle.shape('turtle')
i = 0
a = -35
colors = ['red', 'yellow', 'green', 'blue']# 定义颜色数组
x = turtle.getcanvas().winfo_width()/2
y = turtle.getcanvas().winfo_height()/2


def head(color):
    turtle.pu()
    turtle.goto(0, 50)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pd()
    turtle.seth(-90)
    turtle.circle(80, 360)
    turtle.end_fill()# 定义画脸函数



j = 7
flag = True


def mouth():
    global j, flag
    turtle.pu()
    turtle.goto(0, -65)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(40, 20 + j)
    turtle.pu()
    turtle.goto(0, -65)
    turtle.pd()
    turtle.seth(90)
    turtle.circle(40, -20-j)
    if j > 50 or j < 5:
        flag = not flag
    if flag == True:
        j = j + 3
    else:
        j = j - 3
# 定义画嘴巴函数


def eye(a):
    turtle.pu()
    turtle.goto(-20, 0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 左眼眶
    
    turtle.pu()
    turtle.goto(50, 0)
    turtle.pd()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.seth(0)
    turtle.circle(15, 360)
    turtle.end_fill()# 右眼眶
    
    turtle.pu()
    turtle.goto(a, 0)
    turtle.pd()
    turtle.dot(3)
    turtle.pu()
    turtle.goto(a+70, 0)
    turtle.pd()
    turtle.dot(3)# 左眼珠+右眼珠


def emoji(color, a):
    turtle.clear()
    head(color)
    mouth()
    eye(a)# 定义整体函数


def change(x, y):
    global i
    i += 1
    if i > len(colors) - 1:
        i = 0
    emoji(colors[i], a)
    turtle.update()

def change_eye(event):
    if event.x-x > -300 and event.x-x< -100:
        emoji(colors[i], -45)
    elif event.x-x > 100 and event.x-x < 300:
        emoji(colors[i], -25)
    else:
        emoji(colors[i], -35)
    turtle.update()

emoji(colors[i], -35)


turtle.hideturtle()
turtle.onscreenclick(change, btn=1)
# 点击鼠标后调用函数emoji

cv = turtle.getcanvas()
cv.bind("<Motion>", change_eye)

turtle.done()