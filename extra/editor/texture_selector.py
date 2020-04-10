#! /bin/python3

import tkinter as tk
from tkinter import ttk
from image_frame import *

#This is the raltive directory to the base of the SagoSprite dir
#I am launching from extra/editor so I need to go two levels up
BASEDIR = '../..'

import os
textures = os.listdir(BASEDIR+"/data/textures")
textures = list(filter(lambda x: x.endswith('.png'), textures))


def callback_select(event):
    image = tk.PhotoImage(file=BASEDIR+'/data/textures/'+treeview.selection()[0])
    imageFrame.set_image(image)


root = tk.Tk()
treeview = ttk.Treeview(root)
treeview.pack(expand=tk.YES, fill=tk.BOTH)
for t in textures:
    treeview.insert('','end',t, text = t)
treeview.bind('<<TreeviewSelect>>', callback_select)
imageFrame = ImageFrame(root, None)
imageFrame.get_frame().pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()