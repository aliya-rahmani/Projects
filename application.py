import turtle

# creating window
win = turtle.Screen()
win.bgcolor('black')
win.setup(600,600)

# border turtle
border = turtle.Turtle()
border.speed(8)
border.color('white')
border.width(5)
border.hideturtle()

# text turle
text = turtle.Turtle()
text.color('white')
text.hideturtle()

# spinner turle
s = turtle.Turtle()
s.color('white')
s.hideturtle()
s.width(3)

state = {'turn' : 0}
length = 100
radius = 120

def spinner():
	s.clear()
	angle = state['turn'] / 10
	s.right(angle)
	s.forward(length)
	s.dot(radius, 'red')
	s.dot(10, 'yellow')
	s.back(length)
	s.right(120)
	s.forward(length)
	s.dot(radius, 'green')
	s.dot(10, 'yellow')
	s.back(length)
	s.right(120)
	s.forward(length)
	s.dot(radius, 'blue')
	s.dot(10, 'yellow')
	s.back(length)
	s.right(120)

def animate():
	if state['turn']:
		state['turn'] -= 1

	spinner()
	win.ontimer(animate, 20)

def flick():
	state['turn'] += 40

def stop():
	state['turn'] = 40

# main function
def main():
	border.penup()
	border.goto(-290,290)
	border.pendown()
	for i in range(2):
		border.forward(570)
		border.right(90)
		border.forward(570)
		border.right(90)

	text.penup()
	text.goto(-230,-200)
	text.pendown()
	style = ('Courier',40,'italic')
	text.write('fidget spinner',font=style)

	s.penup()
	s.goto(0,100)
	s.pendown()

	win.tracer(False)
	win.onkey(flick, 'space')
	win.onkey(stop, 'Escape')
	win.listen()
	animate()

	turtle.done()

if __name__ == '__main__':
	main()
