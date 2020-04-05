#! /bin/python3

import tkinter as tk
from tkinter import ttk
from image_frame import *



root = tk.Tk()
image = tk.PhotoImage(file='../../data/textures/terrain.png')
imageFrame = ImageFrame(root, image)
imageFrame.get_frame().pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
