from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import random

# tạo tk window
root= Tk()
root.title('All card forward')
root.geometry('500x630')

# Tên card rồi nhập card vào
deck = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD']

random.shuffle(deck)


def draw(n):
    hand = []
    for i in range(n):
        hand.append(deck.pop())
    return hand


hand = draw(10)

hand.sort()

load_deck = []
render_deck = []

for card in deck:
    load_deck.append(Image.open(f'PNG\\{card}.png'))
    load_deck[-1].thumbnail((150, 150))
    render_deck.append(ImageTk.PhotoImage(load_deck[-1]))

print(load_deck)
print(render_deck)


def kichChuotVaoCard():
    #img.grid_remove()
    img2 = Combobox(root)
    img2['values'] = ('triệu hồi', 'Úp xuống')
    img2.grid(column=0, row=0)
    return

img = Button(root, image=render_deck[0], command=kichChuotVaoCard)
img.grid(column=0, row=0)


root.mainloop()