from Tkinter import *
root = Tk()

canvas_width = 130
canvas_height = 130

w = Canvas(
			root,
			height = canvas_height,
			width = canvas_width)

w.pack()

img = PhotoImage(file = 'pirate.gif')
w.create_image(0,0, anchor = NW, image = img)

root.mainloop()