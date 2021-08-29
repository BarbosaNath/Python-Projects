import json
import tkinter as tk  # noqa
from tkinter import Tk, Label, N, E, W, S, Entry, Text, Button, LEFT, Grid  # noqa
from tkinter import *  # noqa

# Creating Variables
accent_color = '#fde'
accent_dark_color = '#ecd'
bg_color = '#fde'


def delete_word(index, words):
    print(index)
    index = index.cget('text')
    print(index)
    id = 0
    for word in words:
        if index.startswith(word):
            del words[id]
        id += 1
    w = {"words": words}
    with open("words.json", 'w') as json_file:
        json.dump(w, json_file)


def create_buttons(canvas, words, columns):
    i = j = 0
    space = ' '
    for word in words:
        j += 1 if i % columns == 0 else 0
        Grid.rowconfigure(canvas, j+1, weight=1)
        word_buttons.append(Button(canvas, background=accent_color, anchor='w',
                            text=word+f'{(10-len(word))*space}X', bd=0,
                            activebackground=accent_dark_color,
                                   ))

        word_buttons[i].configure(command=lambda:
                                  delete_word(word, words))
        word_buttons[i].grid(column=i % columns, row=j+1,
                             rowspan=1, columnspan=1, sticky=N+S+E+W)
        i += 1
    del space
    return (i, j)


# Create a Window
root = Tk()
root.title('')
root.geometry('300x200')
root.configure(background=bg_color)

# Creating a Grid
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
# Making the grid even
for col in range(6):
    Grid.columnconfigure(root, col, weight=1)


# Getting the JSON info
with open('words.json', 'r') as read_file:
    json_file = json.load(read_file)
words = json_file['words']


# Creating a Label
Label(root, text='Word:', background=accent_color,
      foreground='#000', anchor=W, height=1, width=6).grid(column=0)


# Creating the delete word button
word_buttons = []
buttons_quantity = create_buttons(root, words, 5)

# Creating the add word button
word_buttons.append(Button(root, bg=accent_color, text='Add',
                    bd=0, activebackground=accent_dark_color))
word_buttons[-1].grid(column=4, row=buttons_quantity[1]+1, rowspan=1,
                      columnspan=1, sticky=N+S+E+W)

# Creating a place to add a word
entry = Entry()
Grid.rowconfigure(root, buttons_quantity[1]+2, weight=1)
entry.grid(column=0,     row=buttons_quantity[1]+2,
           columnspan=5, rowspan=2, sticky=N+S+E+W)

del buttons_quantity
root.mainloop()
