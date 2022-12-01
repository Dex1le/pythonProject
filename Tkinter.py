import tkinter
from time import sleep
import keyboard as k
from threading import Thread as thrd
import tkinter as tk
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sys
import tkinter.font as tkFont


window = Tk()
window.title('xyi')
window.resizable(height=False, width=False)
window.geometry('1300x1024')
window['bg'] = 'purple'

label = Label(window, text='А салам алейкум!', width=15, height=9,
              bg='purple', foreground='white', font='Arial, 20'
).pack()

def nacol():
    window2 = Tk()
    window2.title('shaders')
    window2.resizable(height=False, width=False)
    window2.geometry('1300x1024')
    window2['bg'] = 'snow'
    label2 = Label(window2, text='', width=15, height=9,
              bg='snow', foreground='white', font='Arial, 20'
).pack()

def recol():
    window3 = Tk()
    window3.title('skin pack')
    window3.resizable(height=False, width=False)
    window3.geometry('1300x1024')
    window3['bg'] = 'snow'
    label3 = Label(window3, text='', width=15, height=9,
                   bg='snow', foreground='white', font='Arial, 20'
).pack()

frame_for_image3 = tkinter.Frame(
    master=window,
    borderwidth=5,
    width=250,
    height=300
)

file2 = Image.open('81Rxy-KCx2L.png')
resize_i3 = file2.resize((1280,1024))
pick3 = ImageTk.PhotoImage(file2)
panel3 = tk.Label(window, image=pick3)
panel3.place(x=10, y=230)
frame_for_image3.pack()

buttonExample1 = tk.Button(window, bg='red', text='skin pack', command=recol,
                           height=5, width=20, font='Arial').place(x=75, y=100
)

buttonExample2 = tk.Button(window, bg='red', text='shaders', command=nacol,
                           height=5, width=20, font='Arial').place(x=1030, y=100
)

frame_for_image = tkinter.Frame(
    master=window,
    borderwidth=5,
    width=250,
    height=300
)

file1 = Image.open('mine.jpg')
resize_i1 = file1.resize((1280,1024))
pick = ImageTk.PhotoImage(file1)
panel = tk.Label(window, image=pick)
panel.place(x=10, y=230)
frame_for_image.pack()


window.mainloop()