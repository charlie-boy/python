from Tkinter import *
root = Tk()

def fire(event):
	root.after(50,move)

def move():
	x1, y1, x2, y2 = w.coords(id1)
		#print x1, y1
	global dx, dy
	if x1+dx<=0 or x1+dx>=390:
		dx = -dx
	elif y1+dy<=0 or y1+dy>=190:
		dy = -dy

	w.coords(id1, x1+dx, y1+dy, x2+dx, y2+dy)
		
	root.after(5, move)


w = Canvas(
			root,
			height = 200,
			width = 400,
			borderwidth = 0,
			highlightthickness = 0,
			background = 'white')

w.pack()
button1 = Button(root, text = 'Fire!!')
button1.pack()

button1.bind('<Button-1>', fire)
id1 = w.create_oval(3,7,3+10,7+10)

dx = 1
dy = 1 

root.mainloop()