from Tkinter import *
root = Tk()

def paint(event):
	x1, y1 = (event.x-1), (event.y-1)
	x2, y2 = (event.x+1), (event.y+1)
	w.create_oval(x1,y1,x2,y2,fill = "red")

w = Canvas(
			root,
			height = 200,
			width = 200)
root.title("painting")
w.pack(expand = YES, fill = BOTH)
w.bind("<B1-Motion>", paint)

root.mainloop()