# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:38:12 2019

@author: Rafael de Carvalho Bueno
"""

import webbrowser

import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.ttk as tka
from tkinter.filedialog import *
from tkinter import filedialog


def OpenUrl(url):
    webbrowser.open_new(url)

    
def AboutCallBack():
   msg = messagebox.showinfo( "About", " Stratification Generator \n \n Stratification profile generator for Delft3d numerical model \n \n OBS: All data should be specified in a text file from bottom to surface \n\n\n\n Report problems and improvements to email adresss below \n decarvalhobueno@gmail.com\n \n other open-source programs, see \n https://buenorc.github.io/ \n\n\n Rafael de Carvalho Bueno ")    


def salinity_input():
    global path_salinity
    path_salinity = askopenfilename(defaultextension='.txt', filetypes=[('TXT files','*.txt')])

def temperature_input():
    global path_temperature
    path_temperature = askopenfilename(defaultextension='.txt', filetypes=[('TXT files','*.txt')])
    print(path_temperature)

def secondary_input():
    global path_secondary
    path_secondary = askopenfilename(defaultextension='.txt', filetypes=[('TXT files','*.txt')])

def constitent_input():
    global path_constitent
    path_constitent = askopenfilename(defaultextension='.txt', filetypes=[('TXT files','*.txt')])

    

def output_folder():

    global folder_path
    folder_path = filedialog.askdirectory()


def generator():
    
    import stratification as strd
    global path_salinity,path_temperature,path_secondary,path_constitent,folder_path
    
    xm  = mnum.get()
    xn  = nnum.get()
    son = p1.get()
    ton = p2.get()
    seon= p3.get()
    con = p4.get()
    
    
    if son != 1:
        path_salinity = -999

    if ton != 1:
        path_temperature = -999
        
    if seon != 1:
        path_secondary = -999
        
    if con != 1:
        path_constitent = -999

    print(path_temperature)
    strd.main(xm,xn,son,path_salinity,ton,path_temperature,seon,path_secondary,con,path_constitent,folder_path)

def selected_h1():
    global h1_type
    h1_type = int(p1.get())
    
    if int(p1.get()) == 0:
        ha.config(state='disable')
    elif int(p1.get()) ==1:
        ha.config(state='normal')
        
def selected_h2():
    global h2_type
    h2_type = int(p2.get())
    
    if int(p2.get()) == 0:
        hb.config(state='disable')
    elif int(p2.get()) ==1:
        hb.config(state='normal')

def selected_h3():
    global h3_type
    h3_type = int(p3.get())
    
    if int(p3.get()) == 0:
        hc.config(state='disable')
    elif int(p3.get()) ==1:
        hc.config(state='normal')

def selected_h4():
    global h4_type
    h4_type = int(p4.get())
    
    if int(p4.get()) == 0:
        hd['state'] = tk.DISABLED
    elif int(p4.get()) ==1:
        hd['state'] = tk.NORMAL
        
# ---------------------- menu -------------------------------------------------        
window = Tk()

window.title("Stratification generator") 
window.geometry('650x450')

# ----------------------- initial menu ----------------------------------------

menubar = Menu(window)
infomenu = Menu(menubar, tearoff = 0)


infomenu.add_cascade(label = "Code", command = menubar)


url = ''
menubar.add_command(label = "Info",  command = lambda aurl=url:OpenUrl(aurl))
menubar.add_command(label = "About", command = AboutCallBack)
menubar.add_command(label = "Exit",  command = window.destroy)

# ----------------------- Sub-menu --------------------------------------------

mnum = IntVar()
nnum = IntVar()

Label(window, text="Number of grids N").grid(row=2,column=0,pady=4,sticky='w')
nnum = Entry(window, bd =3)
nnum.insert(END,50)
nnum.grid(row=2,column=1,pady=4)

Label(window, text="Number of grids M").grid(row=3,column=0,pady=4,sticky='w')
mnum = Entry(window, bd =3)
mnum.insert(END,50)
mnum.grid(row=3,column=1,pady=4)

      

p1 = IntVar()
p2 = IntVar()
p3 = IntVar()
p4 = IntVar()

h1 = Checkbutton(window,text='Salinity (ppt)', variable=p1, onvalue=1, offvalue=0, command=selected_h1)
h2 = Checkbutton(window,text='Temperature (oC)', variable=p2, onvalue=1, offvalue=0, command=selected_h2)
h3 = Checkbutton(window,text='Secondary Flow (m/s)', variable=p3, onvalue=1, offvalue=0, command=selected_h3) 
h4 = Checkbutton(window,text='Constituent (kg/m3)', variable=p4, onvalue=1, offvalue=0, command=selected_h4) 


h1.grid(row=5,column=0,pady=2,padx=100,sticky='w') 
h2.grid(row=6,column=0,pady=2,padx=100,sticky='w') 
h3.grid(row=7,column=0,pady=2,padx=100,sticky='w') 
h4.grid(row=8,column=0,pady=2,padx=100,sticky='w') 

ha = Button(window,text='Open File',command=salinity_input,state='disable')
ha.grid(row=5,column=1,pady=4,sticky='w')

hb = Button(window,text='Open File',command=temperature_input,state='disable')
hb.grid(row=6,column=1,pady=4,sticky='w')

hc = Button(window,text='Open File',command=secondary_input,state='disable')
hc.grid(row=7,column=1,pady=4,sticky='w')

hd = Button(window,text='Open File',command=constitent_input,state='disable')
hd.grid(row=8,column=1,pady=4,sticky='w')



Label(window,anchor="w", text="Output folder:").grid(row=10,column=0,pady=4,sticky='w')
Button(window,text='Specify Folder',command=output_folder).grid(row=10,column=1,pady=4,sticky='w')

Button(window,font="Verdana 9 bold",text='Generate',command=generator, height = 1, width = 10).grid(row=12,column=1,pady=8,sticky='w')


window.config(menu = menubar)
window.mainloop()