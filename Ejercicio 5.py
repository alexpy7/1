import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.pen(pencolor="red")

def rebote(num):
    for i in range(num):
        t.up()
        t.fd(400)
        t.back(800)
        t.goto(0,0)
        t.left (90)
        t.fd (400)
        t.back (800)
        t.goto (0,0)
        
        
