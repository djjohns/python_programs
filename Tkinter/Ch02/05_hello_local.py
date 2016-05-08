#!/usr/bin/python3
# hello_local.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
#creates the HelloApp class
class HelloApp:
    #creates initialzation fn for the master window
    def __init__(self, master):

        #Sets the label for "Hello,Tkinter" above the buttons    
        self.label = ttk.Label(master, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)

        #sets button posistion for texan hello and what command to execute
        #when the button is clicked
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        #sets button posistion for hawain hello and what command to execute
        #when the button is clicked
        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column = 1)

    #sets button for texan hello to be called on by the Texas button
    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')
    #sets button for hawain hello to be called on by the Hawaii button
    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')

#contstructer method for main fn             
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

#small script to detect if this module is being called directly or
#as part of another program    
if __name__ == "__main__": main()
