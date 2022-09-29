import turtle
import math
import time

turtle.speed(0)


def chess(x, y):
    c1 = "whitesmoke"
    
    for i in range(8):
        turtle.color(c1)
        if c1 == "whitesmoke":
            c1 = "black"
            turtle.color(c1)
        elif c1 == "black":
            c1 = "whitesmoke"
            turtle.color(c1)
        turtle.pu()
        turtle.goto(x, y)
        turtle.pd()
        turtle.pd()
        for i in range(8):

            turtle.begin_fill()
            for i in range(4):
                turtle.forward(75)
                turtle.right(90)

            turtle.end_fill()
            turtle.forward(75)
            if c1 == "whitesmoke":
                c1 = "black"
                turtle.color(c1)
            else:
                c1 = "whitesmoke"
                turtle.color(c1)
        turtle.pu()


        y = y - 75
def man(x,y):
    turtle.color('black')
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.circle(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.goto(x-35, y-50)
    turtle.goto(x+35, y-50)
    turtle.goto(x, y-50)
    turtle.forward(30)
    turtle.goto(x-30,y-130)
    turtle.goto(x,y-80)
    turtle.goto(x+30,y-130)
    #create eyes

    turtle.pu()
    turtle.goto(x-20,y+55)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.pu()
    turtle.goto(x+15,y+55)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.pu()
    turtle.end_fill()
    turtle.goto(x+30,y+30)
    turtle.pd()



    turtle.begin_fill()
    for i in range(180):
        turtle.forward(.5)
        turtle.right(1)

    turtle.right(90)
    turtle.forward(57.5)
    turtle.end_fill()





def purple():

    turtle.addshape('purple-guy-behind.gif')
    turtle.shape('purple-guy-behind.gif')


chess(10,0)
man(0,0)
time.sleep(2)
purple()

turtle.done()












