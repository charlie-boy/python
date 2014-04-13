from Tkinter import *

root = Tk()

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    frame.focus_set()
    print "clicked at", event.x, event.y 

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<B1-Motion>", callback)
frame.pack()

root.mainloop()