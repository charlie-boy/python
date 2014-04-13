from Tkinter import *
root = Tk()

def paint(event):
	x1, y1 = (event.x-1), (event.y-1)
	x2, y2 = (event.x+1), (event.y+1)
	w.create_oval(x1,y1,x2,y2,fill = "red")
	print x1, y1, x2, y2
	L = [str(x1)," ", str(y1)," ", str(x2)," ", str(y2),"\n"]
	f.writelines(L)


w = Canvas(
			root,
			height = 200,
			width = 200)
root.title("painting")
w.pack(expand = YES, fill = BOTH)

f = open("coords.txt", "a")
w.bind("<B1-Motion>", paint)

root.mainloop()

f.close()