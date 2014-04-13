from Tkinter import *
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		button = Button(frame, text = "Quit", fg = "red", command = frame.quit)
		button.pack(side = LEFT)

		hi_there = Button(frame, text = "Hello", command = self.say_hi)
		hi_there.pack(side = LEFT)

	def say_hi(self):
		print "hi there, everyone!"

root = Tk()
app = App(root)
root.mainloop()
root.destroy()	