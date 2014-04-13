from Tkinter import *
root = Tk()
def move():
	global flag
	if flag == 0:
		global dx, dy
		x1, y1, x2, y2 = w.coords(id1)
		#print x1, y1
		if x1+dx<=0 or x1+dx>=190:
			dx = -dx
		elif y1+dy<=0 or y1+dy>=390:
			dy = -dy
		elif (x1+dx==140  or x1+dx ==150) and y1+dy<=150:
			dx = -dx
		w.coords(id1, x1+2*dx, y1+dy, x2+2*dx, y2+dy)
		
		root.after(5, move)

	else:
		pass

def stop(event):
	x1, y1, x2, y2 = w.coords(id1)
	print x1, y1, x2, y2
	global flag
	flag = 1

def move_again(event):
	global flag
	if flag == 1:
		flag = 0
		move()
	else:
		pass
	
	
w = Canvas(
			root,
			height = 400,
			width = 200,
			borderwidth = 0,
			highlightthickness = 0,
			background = 'white')
w.pack()
button1 = Button(root, text = 'stop')
button1.pack()
button2 = Button(root, text = 'move again')
button2.pack()
line = w.create_line(150,0,150,150)

button1.bind('<Button-1>', stop)
button2.bind('<Button-1>', move_again)
dx = 1
dy = 1
flag = 0
id1 = w.create_oval(3,7,3+10,7+10)
root.after(50,move)

root.mainloop()