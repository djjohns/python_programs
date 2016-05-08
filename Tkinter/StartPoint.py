#!/usr/bin/python3
#StartPoint.py by David J. Johns II to aid in faster widget development
#https://github.com/djjohns

#imports Tkinter packages for the GUI
from tkinter import *
#Imports ttk for cross platform support
from tkinter import ttk

#creates the Sample class module
class Sample:
    #creates initialzation FN for the master window
    def __init__(self, master):
        #Place code below



#contstructer method for main FN            
def main():            
    
    root = Tk()
    app = Sample(root)
    root.mainloop()

#small script to detect if this module is being called directly or
#as part of another program    
if __name__ == "__main__": main()
