import turtle

window = turtle.Screen()
turtle.setup(800, 600)
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.left(45)
turtle1.forward(-50)
turtle2.right(45)
turtle2.backward(-50)
turtle1.setposition(-50,-50)
turtle1.left(45)
turtle1.forward(100)
turtle2.setposition(50,-50)
turtle2.right(45)
turtle2.backward(100)
turtle1.hideturtle()
turtle2.hideturtle()

window.mainloop()
