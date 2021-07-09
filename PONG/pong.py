###          Codigo de juego PONG        ###
## Primera version ##
import turtle

##abrimos una ventana
window = turtle.Screen()
window.title("PONG by Xime.") ##Titulo superior de la ventana
window.bgcolor("black") ## Color de fondo
window.setup(width = 800, height = 600) ## Tamaño
window.tracer(0)
###   Marcador   ###
marcadorA = 0
marcadorB = 0

########        Jugadores       #####
##Jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square") ###Nuestro cuadrado tiene 20x20 pixeles 
jugadorA.color("pink")
jugadorA.penup() ##Quitar rastro
jugadorA.goto(-350,0) ##Coordenadas
jugadorA.shapesize(stretch_wid = 5, stretch_len = 1) ##Multiplicamos los 20 pixeles por 5 y por 1
##Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square") 
jugadorB.color("pink")
jugadorB.penup()
jugadorB.goto(350,0) 
jugadorB.shapesize(stretch_wid = 5, stretch_len = 1)
###    PELOTA   ###
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square") ###Nuestro cuadrado tiene 20x20 pixeles 
pelota.color("pink")
pelota.penup()
pelota.goto(0,0)
## Mover la Pelota. La pelota se mueve cada 3 pixeles
pelota.dx = 1
pelota.dy = 1
#### Division ####
division = turtle.Turtle()
division.color("pink")
division.goto(0,400)
division.goto(0,-400)
##PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("JugadorA: 0		JugadorB: 0", align = "center", font=("Courier", 24, "normal"))

##         FUNCIONES        ##
##jugadorA desplazamiento hacia arriba con tecla w
def jugadorA_up():
	y = jugadorA.ycor()
	y += 20
	jugadorA.sety(y)
##jugadorA desplazamiento hacia abajo con tecla s
def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)
##jugadorB desplazamiento hacia arriba con flecha
def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)
##jugadorB desplazamiento hacia abajo con fecla
def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

# CONEXION TECLADO PROGRAMA #
##Aqui llamo a mis funciones y se conectan con el teclado.
window.listen()
window.onkeypress(jugadorA_up, "w")
window.onkeypress(jugadorA_down, "s")
window.onkeypress(jugadorB_up, "Up")
window.onkeypress(jugadorB_down, "Down")

##Bucle principal, donde mi juego va corriendo.
while True:
	window.update()

	pelota.setx(pelota.xcor() + pelota.dx)
	pelota.sety(pelota.ycor() + pelota.dy)


	##Bordes ordenadas
	if pelota.ycor() > 290:
		pelota.dy *= -1
	if pelota.ycor() < -290:
		pelota.dy *= -1


	#Bordes abscisas
	if pelota.xcor() > 390:
		pelota.goto(0,0)
		pelota.dx *= -1
		marcadorA += 1
		pen.clear()
		pen.write("JugadorA: {}      JugadorB: {}".format(marcadorA,marcadorB), align = "center", font=(    "Courier", 24, "normal"))

	if pelota.xcor() < -390:
		pelota.goto(0,0)
		pelota.dx *= -1
		marcadorB += 1
		pen.clear()
		pen.write("JugadorA: {}      JugadorB: {}".format(marcadorA,marcadorB), align = "center", font=(    "Courier", 24, "normal"))

	##Choque con paletas
    # Paleta B
	if ((pelota.xcor() > 340 and pelota.xcor() < 350)
			and (pelota.ycor() < jugadorB.ycor() + 50
			and pelota.ycor() > jugadorB.ycor() - 50)):
		pelota.dx *= -1
    # Paleta A
	if ((pelota.xcor() <-340 and pelota.xcor() > -350)
			and (pelota.ycor() < jugadorA.ycor() + 50
			and pelota.ycor() > jugadorA.ycor() - 50)):
		pelota.dx *= -1
