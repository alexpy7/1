import turtle
import os

#Configurar pantalla

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Dibujar borde

borde_pen = turtle.Turtle()
borde_pen.speed(0)
borde_pen.color("white")
borde_pen.penup()
borde_pen.setposition(-300,-300)
borde_pen.pendown()
borde_pen.pensize(8)
for lado in range(4):
    borde_pen.fd(600)
    borde_pen.lt(90)
borde_pen.hideturtle()

#Crear la tortuga jugadora
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

player_speed = 15

#Crear enemigo
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemy_speed = 2

#Crear bala jugador
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20

#Estado de de la bala
#Preparado para disparar
#La bala esta disparando
bullet_state = "ready"

#Movimientos izq y derecha
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"

    #Mover la bala justo encima del jugador
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()



#Crear uniones de teclado
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    #Mueve al enemigo atras y abajo
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)


    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy_speed *= -1
        enemy.sety(y)

    #Mover bala
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    #Verifica para ver si la bala ha llegado al tope
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"




turtle.exitonclick()
#delay = raw_input("Presiona enter para terminar")
