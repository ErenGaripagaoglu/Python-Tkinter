import tkinter as tk
from tkinter import ttk

def getFunc():
    value1 = textbox1.get() #get value from textbox
        # print(textbox1.get()) 
    label1.config(text= value1) #set value to label
        # label1.config(text= textbox1.get()) 
    textbox1.config(state= 'disabled') #configure properties

def unlockFunc():
    textbox1.config(state='enabled')

#main window
appwindow = tk.Tk()
appwindow.title('Get Set Values')
appwindow.geometry('500x300')

label1 = ttk.Label(master= appwindow, text='Placeholder')
label1.pack()

textbox1 = ttk.Entry(master= appwindow)
textbox1.pack()

button1 = ttk.Button(master= appwindow, text='Button', command= getFunc)
button1.pack()

button2 = ttk.Button(master= appwindow, text='Unlock', command= unlockFunc)
button2.pack()

appwindow.mainloop()