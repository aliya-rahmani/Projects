# Just for fun!!
import turtle
from myturtle import MyTurtle, create_turtles, move_turtles, writer

number_of_turtles = 10

screen = turtle.Screen()

def draw_shape(x, y, n = 30, clear = True):
  if clear:
    writer.clear()
  screen.tracer(0)
  for turtle in screen.turtles():
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
  screen.tracer(1)
  for i in range(n):
    screen.tracer(0)
    move_turtles(screen)
    screen.tracer(1)

create_turtles(screen, number_of_turtles)

draw_shape(0,-150, clear = False)

screen.onclick(draw_shape)

screen.listen()
turtle.done()
