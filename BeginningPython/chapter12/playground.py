from tkinter import *
top = Tk()
def callback(event):
    print(event.x, event.y)

top.bind('<Button-1>', callback)
mainloop()

