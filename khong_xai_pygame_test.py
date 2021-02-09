from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *

# tạo tk window
root= Tk()
root.title('All card forward')
root.geometry('500x630')
load = Image.open('PNG\\2D.png')

load.thumbnail((150, 150))
render = ImageTk.PhotoImage(load)


def handleButton():
    #img.grid_remove()
    img2 = Combobox(root)
    img2['values'] = ('triệu hồi', 'Úp xuống')
    img2.grid(column=0, row=1)
    return

img = Button(root, image=render, command=handleButton)
img.grid(column=0, row=0)


root.mainloop()