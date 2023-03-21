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

FilePaths = []

def OpenFile():
    # Set output
    FilePath = FilePaths[-1]
    AnalysisLabel=Label(app, text="Analyzing now!\n\n Please be patient.\nFITS data can be as large as several GIGABYTES for an image!")
    AnalysisLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
    # Actual work starts here
    hdul = fits.open(FilePath)
    Colormapping = DropDown.get()
    # Iterates over HDULs
    for i in hdul:
        hdul_pos = 0
        try:
            # Grabs image data and checks for
            # NaN array which indicates not an image
            ImageData = hdul[i].data
            Check = ImageData[0][0]
            if np.isnan(Check):
                pass
            else:
                fig = plt.figure(frameon=False)
                ax = plt.Axes(fig, [0.1, 0., 1., 1.])
                ax.set_axis_off()
                fig.add_axes(ax)
                plt.imshow(ImageData, norm=PowerNorm, cmap=Colormapping)
                plt.grid(False)
                cb = plt.colorbar()
                cb.remove()
                fig.show()
        except:
            pass
        hdul_pos += 1

def SelectFile():
    # Ask for and open file
    FileObj=filedialog.askopenfilename()
    FilePath = r"{}".format(FileObj)
    GotLabel=Label(app, text="Selected File: " + str(FilePath))
    GotLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
    FilePaths.append(FilePath)

def Change():
    Colormap.config(text = "Colormap set to: " + DropDown.get())
    Colormapping = DropDown.get()

# Matplotlib setup
plt.style.use(astropy_mpl_style)
PowerNorm = matplotlib.colors.PowerNorm(.4, vmin=3)

# GUI
# Create window
app=Tk()
app.title("Fast FITS Viewer")

# Set res
app.geometry("850x400")

# Create title and put at top
label=Label(app, text="Fast FITS Viewer", font=("Bahnschrift Light", 32))
label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Colormap options
options = [
    "afmhot",
    "gist_heat",
    "bone",
    "Spectral",
    "RdYlBu",
    "RdGy",
    "gnuplot2"
]

DropDown = StringVar()
DropDown.set("afmhot")

# Create Dropdown
drop = OptionMenu(app, DropDown, *options)
drop.place(relx=0.4, rely=0.8, anchor=CENTER)
ChangeColormap = Button(app, text="Set Colormap", command=Change).place(relx=0.6, rely=0.8, anchor=CENTER)

# Display which colormap we switched to
Colormap = Label(app, text = " ")
Colormap.place(relx=0.5, rely=0.7, anchor=CENTER)

# Create select file button + dialogue and put at bottom
EntryButton = tk.Button(app, text="Select File", command=SelectFile)
EntryButton.place(relx=0.4, rely=0.9, anchor=CENTER)

AnalyzeButton = tk.Button(app, text="Analyze File", command=OpenFile)
AnalyzeButton.place(relx=0.6, rely=0.9, anchor=CENTER)

app.mainloop()
