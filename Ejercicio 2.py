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

def cuadrado(parametro):
    '''Función que hace que la tortuga haga un cuadrado con el lado del parámetro'''
    t.forward(parametro)
    t.right(90)
    t.forward(parametro)
    t.right(90)
    t.forward(parametro)
    t.right(90)
    t.forward(parametro)
    t.right(90)

def circulotri(radio,triangulos,lado):
    '''Función que dibuja triángulos en cada x grados'''
    cont = 0
    for i in range(360):
        t.up()
        t.left(1)
        cont = cont + 1
        t.forward(radio)
        t.down()
        if cont == 360/triangulos:
            cont = 0
            triangulo(lado)

#APARTADO B

def cuadradocir(radio,lado):
    cont = 0
    for i in range (360):
        t.up()
        t.left(1)
        cont = cont + 1
        t.forward(radio)
        t.down()
        if cont == 90:
            cont = 0
            cuadrado(lado)
            
