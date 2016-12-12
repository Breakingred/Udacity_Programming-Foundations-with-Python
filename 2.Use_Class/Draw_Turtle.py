import turtle
import os
path=os.getcwd()
print(path)
def draw_square():
    window = turtle.Screen()
    window.bgcolor('gray')
    iris = turtle.Turtle()
    iris.shape('circle')
    iris.color('blue')
    iris.speed(3)
    iris.forward(50)
    iris.right(90)
    iris.forward(50)
    iris.right(90)
    iris.forward(50)
    iris.right(90)
    iris.forward(50)
draw_square()
