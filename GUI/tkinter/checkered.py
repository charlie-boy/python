from Tkinter import *
root = Tk()

def checkered(line_distance):
	x = line_distance
	for i in range(line_distance,canvas_width):
		w.create_line(x,0,x,0+canvas_height)
		w.create_line(0,x,0+canvas_height,x)
		x = x + line_distance
canvas_height = 300
canvas_width = 300


w = Canvas(
			root,
			height = 300,
			width = 300)
w.pack()

root.after(0,checkered(50))
root.mainloop()