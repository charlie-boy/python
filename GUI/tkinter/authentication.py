from Tkinter import *
import webbrowser
import sys

def print_screen():
	txt1 = a.get()
	txt2 = b.get()
	if txt1 == txt2:
		root = Tk()
		t = Text(root)
		t.pack()

		def openHLink(event):
			start, end = t.tag_prevrange("hlink",t.index("@%s,%s" % (event.x, event.y)))
			print "Going to %s..." % t.get(start, end)
			return webbrowser.open(t.get(start, end)) 


		t.tag_configure("hlink", foreground='blue', underline=1)
		t.tag_bind("hlink", "<Button-1>", openHLink)
		t.insert(END, "This is a link\n")
		t.insert(END, "http://www.python.org", "hlink")
		t.insert(END, "\nAnd text goes on...\n")
		labl = Label(root, text = txt1).pack()
		lab2 = Label(root, text = txt2).pack()
		root.geometry('1000x500+500+200')
		root.title("second ")
		root.mainloop()

	return

window1 = Tk()

a = StringVar()
b = StringVar()

window1.geometry('500x500+500+200')
window1.title("Authentication Required!")


username = Label(window1, text = "Username")
password = Label(window1, text = "Password")
text1 = Entry(window1, textvariable = a)
text2 = Entry(window1, textvariable = b)
button = Button(window1, text = "Login", command = print_screen)

username.pack()
text1.pack()
password.pack()
text2.pack()
button.pack()

window1.mainloop()

