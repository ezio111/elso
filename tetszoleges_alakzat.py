# rajzolj egy tetszőleges alakzatot ami nem háromszög és néygszög
# tanuló neptun kód: WNT9SB
import turtle

def rajzol():
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()
    turtle.pencolor("blue")
    turtle.pensize(5)
    turtle.dot(5)
    turtle.pendown()
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
    turtle.dot(5,"red") #jelzi hogy a megfelelő helyen állt meg

#app
ablak=turtle.Screen()

turtle.listen()
turtle.onkey(rajzol,"f")
turtle.onkey(turtle.bye,"d")
turtle.mainloop()