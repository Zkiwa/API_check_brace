#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:56:34 2019

@author: JAJA Abdelkarim

"""
import glob
from tkinter import *
import re
from tkinter import filedialog
import os

# creating a window

window = Tk()
window.title("Window")
window.geometry("500x300")
window.minsize(500, 300)

# ............. The events ............... #
# --------- browser function -------------- #


def browser():
    entry1.delete(0, len(entry1.get()))
    text.delete(1.0, END)
    directory = filedialog.askdirectory(initialdir=os.getcwd(), title="Select a file")
    entry1.insert(END, directory)


# --------- check_braces function -------------- #

def check_braces():
    FOLDER_PATH = entry1.get()
    entry_contents = glob.glob(FOLDER_PATH+"/*.c")

    for file in entry_contents:
        f = open(file, "r")
        lines = f.readlines()

        for i in range(len(lines)):
            if "//" in lines[i]:
                lines[i] = ""
            else:
                if "/*" in lines[i]:
                    lines[i] = ""
                    j = i + 1
                    while "*/" not in lines[j]:
                        lines[j] = " "
                        j += 1
                    lines[j] = " "
        s = ''.join(lines)

        Open_Braces = re.findall('{', s)
        Closed_Braces = re.findall('}', s)

        if len(Open_Braces) == len(Closed_Braces):
            text.insert(END, str(os.path.split(file)[1]) + " : ")
            text.insert(END, "No Errors\n")

        else:
            text.insert(END, str(os.path.split(file)[1])+" : ")
            text.insert(END, "Error found!\n")
            text.insert(END, "\t   - Open Braces : "+str(len(Open_Braces)))
            text.insert(END, "\n\t   - Closed Braces : "+str(len(Closed_Braces))+"\n")

        f.close()


# ............ Creating the widgets :) ................ #

label1 = Label(window, text="C files Dir : ", bg="cyan", font=("New Times", 10))
entry1 = Entry(window, width=40)
Browse_Button = Button(window, text="Browse", command=browser)
Braces_Check_Button = Button(window, text="Braces Check", command=check_braces)
text = Text(window, width=35, height=13, bg='cyan')

# ............ Grid the widgets :) ................ #

label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)
Browse_Button.grid(row=1, column=2)
Braces_Check_Button.grid(row=2, column=1)
text.grid(row=4, column=1)

# ------------------ mainloop ------------------------ #
window.mainloop()
