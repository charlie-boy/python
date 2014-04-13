import Tkinter
import os

window = Tkinter.Tk()

window.title("Jack Sparrow")
window.geometry("300x300")

img = Tkinter.PhotoImage(file='pirate.gif')
window.tk.call('wm', 'iconphoto', window._w, img)

label = Tkinter.Label(window, text = "Pirates of the Carrabian")
text_entry = Tkinter.Entry(window)
button = Tkinter.Button(window, text = "Kill it")

text_entry.pack()
button.pack()
label.pack()
window.mainloop()
