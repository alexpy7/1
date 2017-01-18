import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.pen(pencolor="red")

def poligonos(num,lado):
    '''Función que dibuja cualquier polígono'''
    for i in range(num):
        t.forward(lado)
        t.left(360/num)
        
def circulo_poligonos(num,lado):
    '''Función que dibuja en los vértices invisibles de un polígono ese mismo polígono'''
    for i in range(num):
        poligonos(num,lado)
        t.up()
        t.right(360/num)
        t.forward(50)
        t.down()
   
        

def combi(num,lado,vueltas):
    for i in range (1,vueltas+1):
        for j in range(num):
            circulo_poligonos(num,lado*num)
            t.up()
            t.right(45)
            t.forward(lado*2)
            t.down()
            
