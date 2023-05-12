# ============> Prevent the user from controlling the dimensions of the program and changing the name of the program <===========
# For Import Tkinter Module
from tkinter import *

# To Give Object From Tkinter Module
root = Tk()

# Geometry To Setting A Width And Height of Your Program
# geometry give two Parameter Width And Height
# root.geometry('Width x Height')
# Example This Program Width is 500px And Height is 400px
# root.geometry('300x300')

# If You Want in Open Program By Default Show In Center in Your Monitor
# root.geometry('Width x Height + left + top')
# For Example:
root.geometry('500x400+400+200')

# resizable To Setting A Width And Height of Your Program
# resizable give two Parameter Width And Height And DataType = False,True
# root.resizable(Width , Height','True,False)
# Example This Program Prevent User From Controlling Width
# root.resizable(False,True)
# Example This Program Prevent User From Controlling Height
# root.resizable(True,False)
# Example This Program Prevent User From Controlling Width And Height
root.resizable(False,False)

# root.title For Make Or Change Title of Program
# For Example:
root.title('StayAlive Learn Programming')

# For Open The Program And Loop
root.mainloop()