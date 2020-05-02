import turtle
import time

# canvas setup
wn = turtle.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor("white")
wn.screensize()
wn.setup(width=700, height=700, startx=None, starty=None)
wn.tracer(0)

# wrting pen
pen = turtle.Turtle()
pen.up()
pen.hideturtle()


# welcome screen animates 'Tic' 'Tac' 'Toe' respectively
class welcome_screen:

	pen.goto(-70,-20)
	pen.write("Loading...",font=("Courier",20,"normal"))

	pen.goto(-270,0) 
	pen.write("Tic",font=("Courier",60,"normal"))

	time.sleep(0.6)
	
	pen.goto(-100,0)
	pen.write("Tac",font=("Courier",60,"normal"))

	time.sleep(0.6)
	
	pen.goto(70,0) 
	pen.write("Toe",font=("Courier",60,"normal"))

	time.sleep(1)
	pen.clear()

# defines square object
# properties: shape , size , color
# functions: display x and y corners of a square
class square(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.square = turtle.Turtle()
		self.shape("square")
		self.shapesize(9.9)
		self.color("black")
		self.up()
	
	# display the y coordinates of a square object
	def posy(self):
		posy = []
		pen.goto(self.xcor()-100,self.ycor()+100)
		for i in range(4):
			pen.setheading(-90*i)
			pen.forward(200)
			posy.append(int(pen.ycor()))
		return posy

	# display the x coordinate of a square object
	def posx(self):
		posx=[]
		pen.goto(self.xcor()-100,self.ycor()+100)
		for i in range(4):
			pen.setheading(-90*i)
			pen.forward(200)
			posx.append(int(pen.xcor()))
		return posx

# generate and layout squares in a grid pattren
l = [int(i) for i in range(9)]
p = [-200,0,200]
for i in range(len(l)):
	if i < 3: 
		l[i] = square()
		l[i].goto(p[i],200)
	elif i >= 3 and i < 6: 
		l[i] = square()
		l[i].goto(p[i-3],0)
	else: 
		l[i] = square()
		l[i].goto(p[i-6],-200)

# switches player from red to blue and visversa
player = square()
player.shapesize(1)
player.goto(-250,321)

# inital status of the player when the windows is first opened
player.color("blue")
pen.goto(-190,310)
pen.write("starts",align='center',font=("Courier",15,"normal"))

def switch_player(n,val):

	pen.clear()
	pen.color("black")

	if val == True: 
		l[n].color("blue")
		pen.goto(-200,310)
		pen.write("turn",align='center',font=("Courier",15,"normal"))
		player.color("red")

	else: 
		l[n].color("red")
		pen.goto(-200,310)
		pen.write("turn",align='center',font=("Courier",15,"normal"))
		player.color("blue")

	toggled[n] = 1

# clickable boundaries
# n is the position of the sqaure in the list l
# x,y are coordinate for the cliked position
def boundary_condition(n,x,y): 
	return x < l[n].posx()[0] and x > l[n].posx()[2] and y < l[n].posy()[0] and y > l[n].posy()[2]

# toggled is used to identifies which squares have been played
# 0 means the square has not been played or color has changed
# 1 means the square has been played or color has changed
toggled = [0 for i in range(9)]
toggle = True

# checks for a winner
def check(color):
	# checks rows alignment
	if l[0].color()[0] == l[1].color()[0] == l[2].color()[0] == color: return True
	if l[3].color()[0] == l[4].color()[0] == l[5].color()[0] == color: return True
	if l[6].color()[0] == l[7].color()[0] == l[8].color()[0] == color: return True
	
	# checks column aligment
	if l[0].color()[0] == l[3].color()[0] == l[6].color()[0] == color: return True
	if l[1].color()[0] == l[4].color()[0] == l[7].color()[0] == color: return True
	if l[2].color()[0] == l[5].color()[0] == l[8].color()[0] == color: return True
	
	# checks diagonals aligment
	if l[0].color()[0] == l[4].color()[0] == l[8].color()[0] == color: return True
	if l[2].color()[0] == l[4].color()[0] == l[6].color()[0] == color: return True
	
	# defualt return value
	return False

# displayes the winner then calls replay function after 1500 milliseconds
def display_winner(color):
	
	pen.goto(0,310)
	
	if color == "red":
		pen.color("red")
		pen.write("RED WINS",align='center',font=("TimesNewRoman",15,"bold"))
		wn.ontimer(replay,1500)
		
	if color == "blue":
		pen.color("blue")
		pen.write("BLUE WINS",align='center',font=("TimesNewRoman",15,"bold"))		
		wn.ontimer(replay,1500)

	if color == "none":
		pen.color("black")
		pen.write("NO ONE WINS",align='center',font=("TimesNewRoman",15,"bold"))
		wn.ontimer(replay,1500)

# mouse event handeler
def click(x,y):	

	global toggle

	# switches players until one wins
	if not (check("red") or check("blue")):
		if boundary_condition(0,x,y) and toggled[0] == 0: switch_player(0,toggle)
		if boundary_condition(1,x,y) and toggled[1] == 0: switch_player(1,toggle)
		if boundary_condition(2,x,y) and toggled[2] == 0: switch_player(2,toggle)
		if boundary_condition(3,x,y) and toggled[3] == 0: switch_player(3,toggle)
		if boundary_condition(4,x,y) and toggled[4] == 0: switch_player(4,toggle)
		if boundary_condition(5,x,y) and toggled[5] == 0: switch_player(5,toggle)
		if boundary_condition(6,x,y) and toggled[6] == 0: switch_player(6,toggle)
		if boundary_condition(7,x,y) and toggled[7] == 0: switch_player(7,toggle)
		if boundary_condition(8,x,y) and toggled[8] == 0: switch_player(8,toggle)

		toggle = not toggle

		if check("red"): display_winner("red")
		if check("blue"): display_winner("blue")

	# announce no winners when all sqaure have been played 
	if sum(toggled) == 9 and not (check("red") or check("blue")): display_winner("none")

# resets values for the next game
def replay():
	for i in range(9): 
		l[i].color("black")
		toggled[i] = 0

	pen.clear()

	if check("red"): player.color("blue")
	if check("blue"): player.color("red")

	pen.goto(-190,310)
	pen.color("black")
	pen.write("starts",align='center',font=("Courier",15,"normal"))

# listens for event handler functions
wn.listen()
wn.onclick(click)

# black square at the center for aesthetics
# covers a code glitch lol
center = square()
center.shapesize(1)

# execption handling for program termination
try:
	while True: 
		wn.update()
	
	wn.exitonclick()

except Exception: pass