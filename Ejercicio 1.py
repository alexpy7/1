import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.pen(pencolor="red")

def triangulo (lado):
    '''Función que hace un triángulo'''
    for i in range(3):
        t.forward(lado)
        t.left(120)

def giratri(lado):
    '''Función que recorre el triángulo y lo pinta 6 veces'''
    for i in range(6):
        triangulo(lado)
        t.left(60)

def giratri12(lado):
    for i in range(12):
        triangulo(lado)
        t.left(30)

def giratriangulos(lado,num):
    for i in range(num):
        triangulo(lado)
        t.left(360/num)

def estrella(puntas,lado):
    for i in range(puntas):
        t.forward(lado)
        t.left((puntas//2)*360/puntas)
