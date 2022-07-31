import tkinter
import customtkinter
from SentimentData import *

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np

def searchButton(searchString):
    print("Searching for " + searchString)
    #dataPlot = SentimentData.GetSentimentData(root.tickerInput.get())
    #dataPlot.show()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


root = customtkinter.CTk()
root.title("Stock Sentiment Analysis")
root.geometry("900x600")

#====== Create Panels ======

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Left Panel
root.frame_left = customtkinter.CTkFrame(master=root, width=250, corner_radius=0)
#root.frame_left.grid(row=0, column=0, sticky="nswe")
#root.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing

root.leftColTitle = customtkinter.CTkLabel(master=root.frame_left, text="Search For Company", text_font=("Roboto Medium", -16))
#root.leftColTitle.grid(row=1, column=0, pady=10, padx=10)

root.tickerInput = customtkinter.CTkEntry(master=root.frame_left, width=220, placeholder_text="Company Name or Ticker")
#root.tickerInput.grid(row=2, column=0, pady=10, padx=20)

root.searchBtn = customtkinter.CTkButton(master=root.frame_left, text="Search", command=searchButton(root.tickerInput.get()))
#root.searchBtn.grid(row=3, column=0, pady=5, padx=20)

#Right Panel
root.frame_right = customtkinter.CTkFrame(master=root)


#==========TEST===========

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#==========TEST END===========

# def on_closing(root, event=0):
#     root.destroy()

root.mainloop()
