from Tkinter import *
from tkMessageBox import *
from tkFileDialog import askopenfilename
from tkColorChooser import askcolor

def color():
	result = askcolor()
	print result
def answer():
	showerror("Answer", "Sorry, no answer available")

def callback():
	if askyesno('Verify', 'Really quit?'):
		quit()
		#showwarning('Yes', 'Not yet implemented')
	else:
		showinfo('No', 'Quit has been cancelled')

def reference():
	name = askopenfilename()
	print name

errmsg = 'Error!'
b4 =Button(text = 'Choose color', command = color)
b4.pack()
b3 = Button(text = 'File open',command = reference)
b3.pack(fill = X)
b1 = Button(text = 'Quit', command = callback)
b1.pack(fill = X)
b2 = Button(text = 'Answer', command = answer)
b2.pack(fill = X)
mainloop()