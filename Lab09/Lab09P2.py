import turtle

window = turtle.Screen()
turtle.setup(800,600)
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

turtle1.penup()
turtle1.setposition(0,0)
turtle1.hideturtle()
turtle1.pendown()
turtle1.setposition(0,-100)
turtle2.forward(75)
turtle2.hideturtle()
turtle3.hideturtle()
turtle3.setposition(0,-50)
turtle3.forward(75)

turtle1.hideturtle()
window.mainloop()
