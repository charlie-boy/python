from Tkinter import *
import webbrowser
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
root.mainloop() 
