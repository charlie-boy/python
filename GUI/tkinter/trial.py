from Tkinter import *
master = Tk()

def call():
	print "hello world"

f = Frame(master, height = 100, width = 100)
f.pack_propagate(0)
f.pack()

b = Button(
			f,
			text = 'OK', 
			pady = 10, 
			padx = 10, 
			command = call, 
			activeforeground = "red"
			)

b.config(relief = SUNKEN)

#b = Radiobutton(f,compound = TOP, text = 'click', indicatoron = 0, command = call)
b.pack()
mainloop()