import turtle
import random

def negyszog(x,y):
    #a=5
    #b=4
    ker=2*x+2*y
    ter=x*y
    if x==y:
        alakzat="négyzet"
    else:
        alakzat="téglalap"
    return ker,ter,alakzat

if __name__=="__main__":
    print("Saját hívás")

def negyzet():
    turtle.penup()
    turtle.goto(-50,50)#bal felső
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(5)


    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()
"""
    turtle.goto(50,50)#jobb felső
    turtle.goto(50,-50)#jobb alsó
    turtle.goto(-50, -50)#bal alsó
    turtle.goto(-50, 50)#bal felső
"""

def pont(x,y):
    turtle.goto(x,y)
    turtle.dot(10)

def dobas():
    import random
    turtle.hideturtle()
    turtle.clear()
    negyzet()
    szam=random.randint(1,6)

    if szam==1:
        pont(0,0)
    elif szam==2:
        pont(-25, 25)
        pont(25, -25)
    elif szam==3:
        pont(-25, 0)
        pont(0, 0)
        pont(25, 0)
    elif szam==4:
        pont(-25, 25)
        pont(25, 25)
        pont(25, -25)
        pont(-25, -25)
    elif szam==5:
        pont(0,0)
        pont(-25, 25)
        pont(25, 25)
        pont(25, -25)
        pont(-25, -25)
    elif szam==6:
        pont(-25, 25)
        pont(25, 25)
        pont(25, -25)
        pont(-25, -25)
        pont(25,0)
        pont(-25, 0)


#app
ablak=turtle.Screen()

turtle.listen()
turtle.onkey(dobas,"d")
turtle.onkey(turtle.bye,"Escape")
turtle.mainloop()


