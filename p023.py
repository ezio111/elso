# rajzolj 150 pontos egyenlőszárű háromszöget a képernyő közepére
# a szine legyen piros
#a rajzolás induljon a H betüre
# kilépés legyen Q betü

import turtle


def rajzol():
    turtle.hideturtle()
    turtle.clear()
    turtle.penup()
    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.goto(0, 0)
    turtle.goto(-75,-37.5)
    turtle.pendown()
    for i in range(3):
        turtle.forward(150)
        turtle.left(120)


#app
ablak=turtle.Screen()

turtle.listen()
turtle.onkey(rajzol,"h")
turtle.onkey(turtle.bye,"q")
turtle.mainloop()