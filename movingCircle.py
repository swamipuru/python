from graphics import*
from time import sleep
from  random import randint

def main():
	# create a 200 x 200 graphics window
	win = GraphWin()
	x = randint(2,199)
	y = randint(2,199)
	# create a circle of radius 10 at point (10, 10)
	circle = Circle(Point(x, y), 10)
	#circle.setFill("Red")
	circle.setOutline("black")
	# draw the circle in the graphics window
	circle.draw(win)
	# wait for a mouse click
    #win.getMouse()
	dx = .5
	dy = .5

	for i in range (100000):
		sleep(0.05)
		# move the circle
		circle.move(dx, dy)
		x = x + dx
		y = y + dy
		# when x reaches 190, reverse the direction of movement in
		# the x direction
		if x == 190:
			dx = -1*dx
		else:
			dx = dx
		# when y reaches 190, reverse the direction of movement in
        # the y direction
		if y == 190:
			dy = -1*dy
		else:
			dy = dy
        # when x reaches 10, reverse the direction of movement in
        # the x direction
		if x == 10:
			dx = -1*dx
		else:
			dx = dx
        # when y reaches 10, reverse the direction of movement in
        # the y direction
		if y == 10:
			dy = -1*dy
		else:
			dy = dy
	win.close()
main()

