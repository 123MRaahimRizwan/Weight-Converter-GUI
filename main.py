"""
Project : GUI Weight Converter
@author : M.Raahim Rizwan
Date Created : 22/09/2021
"""

# Importing libraries
from tkinter import *
from tkinter import ttk

# Basic tkinter setup
window = Tk()
window.title("Weight Converter GUI")
window.wm_iconbitmap("Asset/icon.ico")
window.geometry("500x300")

# Creating welcome heading
heading = ttk.Label(window, text="Welcome to Weight Converter", font="lucida 19 bold")
heading.grid(row=0, columnspan=3, padx=70, pady=10)

# Creating entry label (Enter the weight)
entry_label = ttk.Label(window, text="Enter the weight in kg", font="lucida 10")
entry_label.grid(row=1, column=0, padx=40)

# Creating entrybox to enter the weight
user_value = StringVar()
entry_box = ttk.Entry(window, textvariable=user_value)
entry_box.grid(row=1, column=1)


def converter():
	"""
	Handles the conversion
	"""
	gram = float(user_value.get()) * 1000
	pound = float(user_value.get()) * 2.20462
	ounce = float(user_value.get()) * 35.274

	gram_entry.delete("1",END)
	gram_entry.insert(END, gram)

	pound_entry.delete("1",END)
	pound_entry.insert(END, pound)

	ounce_entry.delete("1",END)
	ounce_entry.insert(END, ounce)

# Creating convert button
convert_button = ttk.Button(window, text="Convert", command=converter)
convert_button.grid(row=2, columnspan=3, pady=20)

# Creating gram label
gram_label = ttk.Label(window, text="Gram")
gram_label.grid(row=3, column=0)

# Creating pound label
pound_label = ttk.Label(window, text="Pound")
pound_label.grid(row=4, column=0)

# Creating ounce label
ounce_label = ttk.Label(window, text="Ounce")
ounce_label.grid(row=5, column=0)

# Creating entrybox for grams
gram_entry = ttk.Entry(window)
gram_entry.grid(row=3, columnspan=3, pady=5)

# Creating entrybox for pounds
pound_entry = ttk.Entry(window)
pound_entry.grid(row=4, columnspan=3, pady=5)

# Creating entrybox for ounces
ounce_entry = ttk.Entry(window)
ounce_entry.grid(row=5, columnspan=3, pady=5)

window.mainloop()