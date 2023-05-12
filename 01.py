#   <=============== Geometry <===============

# For Import Tkinter Module
from tkinter import *

# To Give Object From Tkinter Module
root = Tk()

# Geometry To Setting A Width And Height of Your Program
# geometry give two Parameter Width And Height
# root.geometry('Width x Height')
# Example This Program Width is 500px And Height is 400px
root.geometry('300x300')

# If You Want in Open Program By Default Show In Center in Your Monitor
# root.geometry('Width x Height + left + top')
# For Example:
root.geometry('500x400+400+200')

# For Open The Program And Loop
root.mainloop()