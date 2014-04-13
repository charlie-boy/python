import Tkinter
class application(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		# constructor
		# super(app, self).__init__(parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.entryVariable = Tkinter.StringVar(self)
		self.entry = Tkinter.Entry(self)
		self.entry.grid(column = 0, row = 0, sticky = 'EW')
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter text here. ")

		self.button = Tkinter.Button(self, text = u"Click", command = self.OnButtonClick)
		self.button.grid(column = 1, row = 0)

		self.labelVariable = Tkinter.StringVar(self)
		self.label = Tkinter.Label(self, textvariable = self.labelVariable, anchor = 'w', fg = 'white', bg = 'blue')
		self.label.grid(column = 0, row = 1, columnspan = 2, sticky = 'EW')
		self.labelVariable.set(u"Hello")

		self.grid_columnconfigure(0, weight = 1)
		self.resizable(True, False)
		self.update()
		self.geometry(self.geometry())
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)

	def OnButtonClick(self):
		self.labelVariable.set(self.entryVariable.get() + " You clicked the button !")
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)
		#print "You clicked the buttton !"

	def OnPressEnter(self, event):
		self.labelVariable.set(self.entryVariable.get() + " You pressed enter !")
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)
		#print "You pressed enter !"

if __name__ == "__main__":
	app = application(None)
	app.title('My application')
	app.mainloop()