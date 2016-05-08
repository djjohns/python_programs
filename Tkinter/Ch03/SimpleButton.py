#!/usr/bin/python3
#simple button interface
#To be ran inside of a python shell

#imports Tkinter packages for the GUI
from tkinter import *
#Imports ttk for cross platform support
from tkinter import ttk

#Creates the root window for the GUI
root = Tk()

#creates a button that is child to the parent root window
button = ttk.Button(root, text = "Click Me!")

#Packs the button in the graphical manager
button.pack()

#Fn callback to return result of button clicked
def callback():
	print('Yay! You clicked a button!')

#adds the callback FN to the button via command
button.config(command = callback)

#Intersts image into button but will overide the text 
logo = PhotoImage(file = '~/code/Python/Tkinter/Ch03/python_logo.gif')

#Compounds the image with the text, the test justified to the left
button.config(image = logo, compound = LEFT)

#creates a smaller logo using .subsample saved to small_logo
small_logo= logo.subsample(5, 5)

#Replaces the large image with a more appropriate size
button.config(image = small_logo)
