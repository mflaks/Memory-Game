from tkinter import *
import time
import random
from tkinter import messagebox

root = Tk()
root.title('Memory')

root.resizable(0,0)	

# create menu bar

def new_game():
	print('Helo World')

def help():
	messagebox.showinfo('help', 'All of the cards are laid face down on a surface\n'
								'Two cards are flipped face up over each turn.\n'
								'The object of the game is to turn over pairs of matching cards.')


menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Start', command = new_game)
filemenu.add_separator()
filemenu.add_command(label = 'Quit', command = root.quit)

menubar.add_cascade(label = 'File', menu = filemenu)
menubar.add_command(label = 'Help', command = help)

root['menu'] = menubar


# create the Canvas

# USA
canvas1 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'red')
canvas1.create_rectangle(0,0,40,40, fill= 'blue', outline = 'blue')
canvas1.create_rectangle(40,8,140,12, fill= 'white', outline = 'white')
canvas1.create_rectangle(40,18,140,22, fill= 'white', outline = 'white')
canvas1.create_rectangle(40,29,140,33, fill= 'white', outline = 'white')
canvas1.create_rectangle(0,40,140,44, fill= 'white', outline = 'white')
canvas1.create_rectangle(0,51,140,55, fill= 'white', outline = 'white')
canvas1.create_rectangle(0,62,140,66, fill= 'white', outline = 'white')
canvas1.create_rectangle(0,73,140,77, fill= 'white', outline = 'white')
canvas1.create_rectangle(4,4,5,5, fill= 'white', outline = 'white')
canvas1.create_rectangle(14,4,15,5, fill= 'white', outline = 'white')
canvas1.create_rectangle(24,4,25,5, fill= 'white', outline = 'white')
canvas1.create_rectangle(34,4,35,5, fill= 'white', outline = 'white')
canvas1.create_rectangle(7,14,8,15, fill= 'white', outline = 'white')
canvas1.create_rectangle(17,14,18,15, fill= 'white', outline = 'white')
canvas1.create_rectangle(27,14,28,15, fill= 'white', outline = 'white')
canvas1.create_rectangle(4,24,5,25, fill= 'white', outline = 'white')
canvas1.create_rectangle(14,24,15,25, fill= 'white', outline = 'white')
canvas1.create_rectangle(24,24,25,25, fill= 'white', outline = 'white')
canvas1.create_rectangle(34,24,35,25, fill= 'white', outline = 'white')
canvas1.create_rectangle(7,34,8,34, fill= 'white', outline = 'white')
canvas1.create_rectangle(17,34,18,35, fill= 'white', outline = 'white')
canvas1.create_rectangle(27,34,28,35, fill= 'white', outline = 'white')

canvas2 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'red')
canvas2.create_rectangle(0,0,40,40, fill= 'blue', outline = 'blue')
canvas2.create_rectangle(40,8,140,12, fill= 'white', outline = 'white')
canvas2.create_rectangle(40,18,140,22, fill= 'white', outline = 'white')
canvas2.create_rectangle(40,29,140,33, fill= 'white', outline = 'white')
canvas2.create_rectangle(0,40,140,44, fill= 'white', outline = 'white')
canvas2.create_rectangle(0,51,140,55, fill= 'white', outline = 'white')
canvas2.create_rectangle(0,62,140,66, fill= 'white', outline = 'white')
canvas2.create_rectangle(0,73,140,77, fill= 'white', outline = 'white')
canvas2.create_rectangle(4,4,5,5, fill= 'white', outline = 'white')
canvas2.create_rectangle(14,4,15,5, fill= 'white', outline = 'white')
canvas2.create_rectangle(24,4,25,5, fill= 'white', outline = 'white')
canvas2.create_rectangle(34,4,35,5, fill= 'white', outline = 'white')
canvas2.create_rectangle(7,14,8,15, fill= 'white', outline = 'white')
canvas2.create_rectangle(17,14,18,15, fill= 'white', outline = 'white')
canvas2.create_rectangle(27,14,28,15, fill= 'white', outline = 'white')
canvas2.create_rectangle(4,24,5,25, fill= 'white', outline = 'white')
canvas2.create_rectangle(14,24,15,25, fill= 'white', outline = 'white')
canvas2.create_rectangle(24,24,25,25, fill= 'white', outline = 'white')
canvas2.create_rectangle(34,24,35,25, fill= 'white', outline = 'white')
canvas2.create_rectangle(7,34,8,34, fill= 'white', outline = 'white')
canvas2.create_rectangle(17,34,18,35, fill= 'white', outline = 'white')
canvas2.create_rectangle(27,34,28,35, fill= 'white', outline = 'white')

# BRAZIL
canvas3 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'green')
canvas3.create_polygon(10,40,70,70, 130,40,70,10, fill= 'yellow', outline = 'yellow')
canvas3.create_oval(40,20,100 ,60, fill= 'blue', outline = 'blue')
canvas3.create_arc(40,35,100,55, fill = 'white', width = 5, style= 'arc', outline = 'white', start= 0 , extent = 180)

canvas4 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'green')
canvas4.create_polygon(10,40,70,70, 130,40,70,10, fill= 'yellow', outline = 'yellow')
canvas4.create_oval(40,20,100 ,60, fill= 'blue', outline = 'blue')
canvas4.create_arc(40,35,100,55, fill = 'white', width = 5, style= 'arc', outline = 'white', start= 0 , extent = 180)

# JAPAN
canvas5 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas5.create_oval(40,20,100,60, fill = 'red', outline = 'red')

canvas6 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas6.create_oval(40,20,100,60, fill = 'red', outline = 'red')

# ISRAEL
canvas7 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas7.create_rectangle(0,10,140,20, fill = 'blue', outline = 'blue')
canvas7.create_rectangle(0,60,140,70, fill = 'blue', outline = 'blue')
canvas7.create_polygon(70,26,50,50,90,50, outline = 'blue', width = 2, fill = '')
canvas7.create_polygon(70,55,50,35,90,35, outline = 'blue', width = 2, fill = '')

canvas8 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas8.create_rectangle(0,10,140,20, fill = 'blue', outline = 'blue')
canvas8.create_rectangle(0,60,140,70, fill = 'blue', outline = 'blue')
canvas8.create_polygon(70,26,50,50,90,50, outline = 'blue', width = 2, fill = '')
canvas8.create_polygon(70,55,50,35,90,35, outline = 'blue', width = 2, fill = '')

# ITALY
canvas9 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas9.create_rectangle(0,0,45,80, outline = 'green', fill = 'green')
canvas9.create_rectangle(45,0,93,80, outline = 'white', fill = 'white')
canvas9.create_rectangle(93,0,140,80, outline = 'red', fill = 'red')

canvas10 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas10.create_rectangle(0,0,45,80, outline = 'green', fill = 'green')
canvas10.create_rectangle(45,0,93,80, outline = 'white', fill = 'white')
canvas10.create_rectangle(93,0,140,80, outline = 'red', fill = 'red')

# FRANCE
canvas11 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas11.create_rectangle(0,0,45,80, outline = 'green', fill = 'blue')
canvas11.create_rectangle(45,0,93,80, outline = 'white', fill = 'white')
canvas11.create_rectangle(93,0,140,80, outline = 'red', fill = 'red')

canvas12 = Canvas(root, width = 140, height = 80, bd = 0 , highlightthickness = 1, bg= 'white')
canvas12.create_rectangle(0,0,45,80, outline = 'green', fill = 'blue')
canvas12.create_rectangle(45,0,93,80, outline = 'white', fill = 'white')
canvas12.create_rectangle(93,0,140,80, outline = 'red', fill = 'red')


list_canvas = [(canvas1, 'usa'), (canvas2, 'usa'),(canvas3, 'brazil'), (canvas4, 'brazil'),(canvas5, 'japan'), (canvas6,'japan'),(canvas7, 'israel'), (canvas8, 'israel'),(canvas9, 'italy'), (canvas10, 'italy'),(canvas11, 'france'), (canvas12, 'france')]

random.shuffle(list_canvas)


open_cards = []

class Card(Button):

	def __init__(self, window, row_card, column_card, canvas, canvas_pos, id, card_name):
		Button.__init__(self, window)
		self['bg'] = 'light blue'
		self['width'] = 20
		self['height'] = 5
		self['text'] = ''
		self.row_card = row_card
		self.column_card = column_card
		self.canvas = canvas
		self.canvas_pos = canvas_pos
		self.id_canvas = id
		self.card_name = card_name
		self.grid(row = self.row_card, column = self.column_card)

		def click():
			global check
			global count
			print(self)
			global open_cards
			self.grid_forget()
			self.canvas.grid(row = row_card , column = column_card)
			open_cards.append(list_canvas[canvas_pos][1])
			open_cards.append(self.card_name)
			check()
			
		self['command'] = click
		
						

card1 = Card(root,0,0,list_canvas[0][0],0,list_canvas[0][1], 'card1')
card2 = Card(root,0,1,list_canvas[1][0],1,list_canvas[1][1], 'card2')
card3 = Card(root,0,2,list_canvas[2][0],2,list_canvas[2][1], 'card3')
card4 = Card(root,1,0,list_canvas[3][0],3,list_canvas[3][1], 'card4')
card5 = Card(root,1,1,list_canvas[4][0],4,list_canvas[4][1], 'card5')
card6 = Card(root,1,2,list_canvas[5][0],5,list_canvas[5][1], 'card6')
card7 = Card(root,2,0,list_canvas[6][0],6,list_canvas[6][1], 'card7')
card8 = Card(root,2,1,list_canvas[7][0],7,list_canvas[7][1], 'card8')
card9 = Card(root,2,2,list_canvas[8][0],8,list_canvas[8][1], 'card9')
card10 = Card(root,3,0,list_canvas[9][0],9,list_canvas[9][1], 'card10')
card11 = Card(root,3,1,list_canvas[10][0],10,list_canvas[10][1], 'card11')
card12 = Card(root,3,2,list_canvas[11][0],11,list_canvas[11][1], 'card12')


cards = [card1, card2, card3, card4,card5, card6, card7, card8, card9, card10, card11, card12 ]

count = 0

def check():
	global count 
	root.update()
	count = count + 1
	if count % 2 == 0:
		print(count % 2)
		for i in cards:
			if open_cards.count(i.id_canvas) ==1 and open_cards.count(i.card_name)==1:
				time.sleep(0.5)
				i.grid(row = i.row_card, column = i.column_card)
				open_cards.remove(i.id_canvas)
				open_cards.remove(i.card_name)
				root.update()
				

				
				
				
root.update()		
root.mainloop()
