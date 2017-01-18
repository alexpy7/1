import turtle
s = turtle.Screen()
t = turtle.Turtle()
#t.shape('turtle')

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

def bucle_cuadrado(parametro, numero):
    '''Función que hace que la tortuga pinte un cuadrado numero de veces con el parametro que le demos, aumentando las unidades'''
    for i in range (numero):
        cuadrado(parametro * i)

def bucle_bonito(parametro):
    '''Pinta cuatro cuadrados'''
    for i in range (4):
        cuadrado(parametro)
        t.right(90)

def giracuadros(lado,num,grado):
    '''Hace los lados de la medida que queramos, el número de veces que queramos con los grados que queramos'''
    for i in range (1,num+1):
        cuadrado(lado)
        t.right(grado)
