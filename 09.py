# ============> ComboBox <===========
# For Import Tkinter Module
from tkinter import *
from tkinter import ttk

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
# root.resizable(False,False)

# root.title For Make Or Change Title of Program
# For Example:
root.title('StayAlive Learn Programming')

# root.config For Make Or Change Style Your Programming
# For Example, Make/Change Programming Background:
# Notes root.config Respect Hexadecimal And ACSI
root.config(background='#DDD')
# For Example, Make/Change Programming Icone:
#root.iconbitmap('D:\Ziad\programming\Courses\Python\Tkinter-Module\src-learn\logo.ico')
#               OR
#root.iconbitmap('D:\\Ziad\programming\\Courses\\Python\\Tkinter-Module\\src-learn\\logo.ico')
#               OR
root.iconbitmap('./logo.ico')

# To Make The Minimum Or Maximum Of Screen
root.minsize(300,250)
root.maxsize(500,400)

# Frame same Function Divide the program into several sections
# Frame Will Get Width And Height Other Style
frame1 = Frame (width='250',height='300',bg='Red')
frame1.place(x=0,y=0)
frame2 = Frame (width='250',height='300',bg='Blue')
frame2.place(x = 250,y = 0)
frame3 = Frame (width='500',height='100',bg='Green')
frame3.place(x=0,y=300)

# ============> Button <==============

Redbutton = Button(frame1,width='15',text='Red Button',fg='Black',bg='white')
Redbutton.place(x=75,y=150)

Bluebutton = Button(frame2,text='Blue Button',fg='Black',bg='white')
Bluebutton.place(x=75,y=150)

GreenButton = Button(frame3,text='Green Button',fg='Black',bg='white',font=10)
GreenButton.place(x=207.5,y=30)

# ======> Label <===========
Label1 = Label (frame1,text='Hello, From Label',fg='White',bg='Black',font=10)
Label1.place(x=1,y=1)

# ===========> Entry => Input <============

username = Entry(frame1,justify='center',bg='White',fg='Black',font=7.5)
username.place(x=30,y=125)

# ==========> ComboBox <============
Gender = ttk.Combobox(frame1,
                     value=('Male','Female'),state='readonly'
)
Gender.place(x=80,y=70)

LabelGender = Label(frame1,width='8',text='Gender: ',bg='Black',fg='White')
LabelGender.place(x=17.5,y = 70)
# For Open The Program And Loop
root.mainloop()