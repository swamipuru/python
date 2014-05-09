from Tkinter import *
import Tkinter
import random
import tkMessageBox

class Die:
	def __init__(self, initVal, master):
		self.value = initVal
		self.display = Tkinter.Label(master, relief="ridge", borderwidth=2, text=self.value, font=("Courier New", 30))

	def roll(self):
		self.value = random.randrange(1,7)
		self.display.config(text = str(self.value))


score1 = 100
score2 = 100
turn1 = 0
turn2 = 0
def rollAll(Dice,row1,row2,row3,row4,row5,message,coin,player):
	global turn1
	global turn2
	print(turn1,'  ',turn2)
	if player == 1:
		turn2 = 0
	else:
		turn1 = 0
	if turn1 > 1:
			tkMessageBox.showwarning('Player 2 turn')
	elif  turn2 > 1:
			tkMessageBox.showwarning('Player 1 turn')
	elif turn1 < 2 or turn2 < 2 :
		avail = int(coin['text'][:-1])
		earn = 0
		for i in range(5):
			Dice[i].roll()

		if row1.value == row2.value == row3.value or row2.value == row3.value == row4.value or row3.value == row4.value == row5.value:
			message.config(text="3 of a Kind.")
			earn = 8
		elif row1.value == row2.value == row3.value == row4.value or row2.value == row3.value == row4.value == row5.value:
			message.config(text="4 of a Kind.")
			earn = 15
		elif row1.value == row2.value == row3.value == row4.value == row5.value:
			message.config(text="5 of a Kind.")
			earn = 30
		elif row1.value == row2.value or row2.value == row3.value or row3.value == row4.value or row4.value == row5.value:
			message.config(text="One Pair.")
			earn = 5
		elif row1.value == row2.value == row3.value and row4.value == row5.value or row3.value == row4.value == row5.value and row1.value == row2.value:
			message.config(text='One Pair and 3 of a Kind.')
			earn = 20
		else:
			message.config(text='Nothing useful.')
		avail  = avail - 10 + earn
		coin.config(text=str(avail)+'$')
		if(player == 1):
			global score1
			score1 = avail
			turn1  += 1
			turn2 = 0
		else:
			global score2
			score2 = avail
			turn2 += 1
			turn1 = 0
		if avail < 10:
			top = Tkinter.Toplevel(bg = 'cyan')
			ws = top.winfo_screenwidth()
			hs = top.winfo_screenheight()
			top.geometry('%dx%d+%d+%d'%(ws/6,hs/6,ws/4,hs/4))
			top.lift()
			top.overrideredirect(2)
			label0 = Tkinter.Label(top,text='',bg = 'brown',fg='green',font=("Courier New", 20))
			label0.pack()
			btn = Tkinter.Button(top,text='OK',bg = 'cyan',command=top.quit,width=10,height=10).pack()
			if(score1 > score2):
				label0.config(text='Player 1 won')
			elif score1 == score2 :
				label0.config(text='Game Draw')
			else:
				label0.config(text='Player 2 won')


def play():
	gameWindow = Tkinter.Tk()
	gameWindow.title("Dice Poker")
	ws = gameWindow.winfo_screenwidth()
	hs = gameWindow.winfo_screenheight()
	gameWindow.geometry('%dx%d+%d+%d'%(ws/2,hs/3,ws/5,hs/5))
	gameWindow.lift()
	gameWindow.resizable(width=TRUE,height=TRUE)

	frameP1 = Tkinter.PanedWindow(gameWindow)
	frame1 = PanedWindow(frameP1)

	Tkinter.Label(frameP1,text='player1',font=("Courier New", 30)).pack()
	coinsP1 = Tkinter.Label(frameP1,text='100$',font=("Courier New", 30))
	coinsP1.pack()
	frameP1.pack()

	row11=Die(1, frame1)
	row11.display.pack(side="left")
	row12=Die(1, frame1)
	row12.display.pack(side="left")
	row13=Die(1, frame1)
	row13.display.pack(side="left")
	row14=Die(1, frame1)
	row14.display.pack(side="left")
	row15=Die(1, frame1)
	row15.display.pack(side="left")
	frame1.pack()
	messageP1=Tkinter.Label(frameP1, text = " ",font=("Courier New", 30),width=15)
	messageP1.pack()
	Dice1 = [row11, row12, row13, row14, row15]

	button=Tkinter.Button(frameP1, command=lambda: rollAll(Dice1,row11,row12,row13,row14,row15,messageP1,coinsP1,1), text="Roll", width=5, height=10,font=("Courier New", 20))
	button.pack()
	frameP1.pack(side='left')



	frameP2 = Tkinter.PanedWindow(gameWindow)
	frame2 = PanedWindow(frameP2)

	Tkinter.Label(frameP2,text='Player2',font=("Courier New", 30)).pack()
	coins = Tkinter.Label(frameP2,text='100$',font=("Courier New", 30))
	coins.pack()
	frameP2.pack()

	row1=Die(1, frame2)
	row1.display.pack(side="left")
	row2=Die(1, frame2)
	row2.display.pack(side="left")
	row3=Die(1, frame2)
	row3.display.pack(side="left")
	row4=Die(1, frame2)
	row4.display.pack(side="left")
	row5=Die(1, frame2)
	row5.display.pack(side="left")
	frame2.pack()
	messageP2=Tkinter.Label(frameP2, text = " ", font=("Courier New", 30),width=15)
	messageP2.pack()
	Dice2 = [row1, row2, row3, row4, row5]

	button=Tkinter.Button(frameP2, command=lambda: rollAll(Dice2,row1,row2,row3,row4,row5,messageP2,coins,2), text="Roll", width=5, height=10,font=("Courier New", 20))
	button.pack()
	frameP2.pack(side='right')


	button=Tkinter.Button(gameWindow,command=gameWindow.quit,text="STOP")
	button.pack(side=BOTTOM)

	print(int(coinsP1['text'][:-1]))
	print(int(coins['text'][:-1]))

	gameWindow.mainloop()




if __name__ == '__main__':
	root = Tk()
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	root.wm_title('Dice Poker Game')
	root.geometry('%dx%d+%d+%d'%(ws/3,hs/3,ws/5,hs/5))
	root.lift()
	root.resizable(width=TRUE,height=TRUE)
	frame = PanedWindow(root)
	frame.pack(fill=BOTH)

	btnPlay = Button(frame,text='Play    ',command=play)
	btnExit = Button(frame,text='Exit',command=root.quit)
	btnPlay.pack(side=TOP)
	btnExit.pack(side=TOP)
	root.mainloop()
