#! /bin/python3

import tkinter as tk
from tkinter import ttk
from image_frame import *
from tree_frame import *

#This is the raltive directory to the base of the SagoSprite dir
#I am launching from extra/editor so I need to go two levels up
BASEDIR = '../..'

import os
#textures_filenames = os.listdir(BASEDIR+"/data/textures")
#textures = list(filter(lambda x: x.endswith('.png'), textures_filenames))
#textures.sort()


def addFolderToList(theFolder, theList):
    textures_filenames = os.listdir(BASEDIR+"/data/textures/"+theFolder)
    for x in textures_filenames:
        if x.endswith('.png'):
            theList.append(theFolder+"/"+x)
    folders = list(filter(lambda x: os.path.isdir(BASEDIR+"/data/textures/"+theFolder+"/"+x), textures_filenames))
    print(folders)
    for f in folders:
        addFolderToList(theFolder+"/"+f, theList)


textures = []
addFolderToList("", textures)
#folders = list(filter(lambda x: os.path.isdir(BASEDIR+"/data/textures/"+x), textures_filenames))
#addFolderToList()
#print(folders)


def callback_select(event):
    image = tk.PhotoImage(file=BASEDIR+'/data/textures/'+treeview.selection()[0])
    imageFrame.set_image(image)


root = tk.Tk()
treeFrame = TreeFrame(root)
treeview = treeFrame.get_treeview()
treeFrame.get_frame().grid(row=0, column=0, sticky='ns')
for t in textures:
    treeview.insert('','end',t, text = t)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
treeview.bind('<<TreeviewSelect>>', callback_select)

imageFrame = ImageFrame(root, None)
imageFrame.get_frame().grid(row=0, column=1, sticky='nsew')

root.mainloop()