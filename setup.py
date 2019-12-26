#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:56:34 2019

@author: JAJA Abdelkarim
"""

from tkinter import *
import re
from tkinter import filedialog
import os

window = Tk()
window.title("JAJA")
window.geometry("450x300")


def browser():
    directory = filedialog.askdirectory(initialdir=os.getcwd(), title="Select a file")
    entry1.insert(END, directory)


def check_braces():
    FOLDER_PATH = entry1.get()
    entry_contents = os.listdir(FOLDER_PATH)
    for file in entry_contents:
        filename = os.path.abspath(os.path.join(FOLDER_PATH, file))
        f = open(filename, "r")
        print(f.name)
        liste = f.readlines()
        for str1 in liste:
            print(str1)

        #if not (liste.startswith('/*', 0, len(liste)) or liste.endswith('*/', 0, len(liste)) or liste.startswith('//', 0, len(liste))):
        s = ''.join(liste)
        Open_Braces = re.findall('{', s)
        Closed_Braces = re.findall('}', s)

        if len(Open_Braces) == len(Closed_Braces):
            text.insert(END, str(file) + " : ")
            text.insert(END, "No Errors\n")
            entry1.delete(0, END)

        else:
            text.insert(END, ""+str(file)+" : ")
            text.insert(END, "Error found!\n")
            text.insert(END, "\t   - Open Braces : "+str(len(Open_Braces)))
            text.insert(END, "\n\t   - Closed Braces : "+str(len(Closed_Braces))+"\n")


label1 = Label(window, text="C files Dir", bg="cyan")
entry1 = Entry(window)

Browse_Button = Button(window, text="Browse", command=browser)
Braces_Check_Button = Button(window, text="Braces Check", command=check_braces)
text = Text(window, width=35, height=10)

label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)
Browse_Button.grid(row=1, column=2)
Braces_Check_Button.grid(row=2, column=1)
text.grid(row=4, column=1)

window.mainloop()
