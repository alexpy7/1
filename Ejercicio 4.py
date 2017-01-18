import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
from random import randint

def poligonos(num,lado):
    '''Función que dibuja cualquier polígono'''
    for i in range(num):
        t.forward(lado)
        t.left(360/num)

colores = ['gold','tomato4','red','deep pink','orchid','dodger blue','black','orange2','purple1','turquoise 1']

def pintapol(vertices,lado,num):
    '''Pinta poligonos num veces dentro del primero y los colorea aleatoriamente'''
    for i in range (1,num+1):
        t.fillcolor(colores[randint(0,i)])
        t.begin_fill()
        poligonos(vertices,lado-3*i)
        t.end_fill()
       

def bucletotal(num,lado):
    '''Dibuja los poligonos num de veces, los borra y pone el siguiente hasta llegar a num'''
    for i in range (3,num+1):
        pintapol(i,lado,5)
        t.reset()

