import turtle
#import time
a = turtle.Turtle()
b = turtle.Turtle()
b.color('green') 
b.shape('turtle')
a.color('green') 
a.shape('turtle')
for i in range(720):
    a.forward(1)
    a.left(0.5)
    b.forward(1)
    b.right(0.5)