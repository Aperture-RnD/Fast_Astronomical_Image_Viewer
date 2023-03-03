# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:48:58 2023
Spaaaaaaaaaaaaaaaaaaaaace!
@author: wbender
"""

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
import numpy as np

def OpenFile():
    FileObj=filedialog.askopenfilename()
    FilePath = r"{}".format(FileObj)
    testlabel=Label(app, text="Analyzing now!\n\n Please be patient.\nFITS data can be as large as several GIGABYTES for an image! \n\n The file you selected (MUST be .fits extenstion!): \n" + str(FileObj))
    testlabel.place(relx=0.5, rely=0.6, anchor=CENTER)
   # print(FilePath)
    hdul = fits.open(FilePath)
    print("Filepath: " + FilePath)
    for i in hdul:
        hdul_pos = 0
        try:
            ImageData = hdul[i].data
            Check = ImageData[0][0]
            if np.isnan(Check):
                pass
            else:
                fig = plt.figure(frameon=False)
                ax = plt.Axes(fig, [0.1, 0., 1., 1.])
                ax.set_axis_off()
                fig.add_axes(ax)
                plt.imshow(ImageData, norm=PowerNorm, cmap='afmhot')
                plt.grid(False)
                cb = plt.colorbar()
                cb.remove()
                fig.show()
        except:
            pass
        hdul_pos += 1

#matplotlib setup
plt.style.use(astropy_mpl_style)
PowerNorm = matplotlib.colors.PowerNorm(.4, vmin=3)

#GUI
# Create window
app=Tk()
app.title("Fast FITS Viewer")

# Set geometry
app.geometry("600x300")

# Create title and put at top
label=Label(app, text="Fast FITS Viewer", font=("Bahnschrift Light", 32))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Create select file button + dialogue and put at bottom
EntryButton = tk.Button(app, text="Select File", command=OpenFile)
EntryButton.place(relx=0.5, rely=0.9, anchor=CENTER)

app.mainloop()
