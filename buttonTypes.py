import tkinter as tk
from tkinter import ttk

#create
appwindow = tk.Tk()
appwindow.title('Button Types')
appwindow.geometry('400x300')

#button
button1 = ttk.Button(master= appwindow, text= 'Button', command= lambda: print('Button Pressed'))
button1.pack()

#checkbox
chckVar = tk.BooleanVar() #store and reach checkbox state
checkbox1 = ttk.Checkbutton(appwindow, text= 'Checkbox1 Text',variable= chckVar ,command= lambda: print('Checkbox Checked Changed', chckVar.get()))
checkbox1.pack()                                           #connection with var

#radiobutton
def radioSelected():
    print('Selected Radiobutton is',radioVar.get())

radioVar = tk.IntVar()
radiobutton1 = ttk.Radiobutton(appwindow, text= 'Radiobutton1', value= 1, variable= radioVar, command= radioSelected)
radiobutton2 = ttk.Radiobutton(appwindow, text= 'Radiobutton2', value= 2, variable= radioVar, command= radioSelected)

radiobutton1.pack()
radiobutton2.pack()

#run
appwindow.mainloop()