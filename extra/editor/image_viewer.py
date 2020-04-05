#! /bin/python3

import tkinter as tk
from tkinter import ttk


class ImageFrame:
    def __init__(self, master, image):
        self.frame = ttk.Frame(master)
        self.canvas = tk.Canvas(self.frame)
        self.xscroll = ttk.Scrollbar(self.frame, orient = tk.HORIZONTAL, command = self.canvas.xview)
        self.yscroll = ttk.Scrollbar(self.frame, orient = tk.VERTICAL, command = self.canvas.yview)
        self.canvas.grid(row=1, column= 0, sticky= 'nsew')
        self.frame.columnconfigure(0, weight = 1)
        self.frame.rowconfigure(1, weight = 1)
        self.xscroll.grid(row = 2, column=0, sticky = 'ew')
        self.yscroll.grid(row = 1, column=2, sticky = 'ns')
        self.canvas.config(xscrollcommand = self.xscroll.set, yscrollcommand = self.yscroll.set)
        self.setImage(image)

    def setImage(self, image):
        self.image_file = image
        self.canvas.create_image(0, 0, image=self.image_file, anchor=tk.NW)
        self.canvas.config(scrollregion = (0, 0, self.image_file.width(), self.image_file.height()))

    def getFrame(self):
        return self.frame

root = tk.Tk()
image = tk.PhotoImage(file='../../data/textures/terrain.png')
imageFrame = ImageFrame(root, image)
imageFrame.getFrame().pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()