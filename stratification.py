# -*- coding: utf-8 -*-
"""
@author: rafael de carvalho bueno

"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from tkinter import *
from matplotlib import gridspec


class StdoutRedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert(END, str)
        self.text_area.see(END)


def main (m,n,son,sal,ton,tau,seon,sec,con,const,folder_path):

    old_stdout = sys.stdout
    
    root = Tk()
    root.configure(background='white')
    root.title("Generator running") 
    root.geometry('450x500')

    outputPanel = Text(root, wrap='word', height=30, width=100)
    outputPanel.grid(column=0, row=0, columnspan = 2, sticky='NSWE', padx=5, pady=5)

    # input data
    n    = int(n)
    m    = int(m)
    
    if son==1:
        sali = np.loadtxt(sal)
        layers = len(sali)
    if ton==1:
        temp = np.loadtxt(tau)
        layers = len(temp)
    if seon==1:
        seco = np.loadtxt(sec)
        layers = len(seco)
    if con==1:
        cons = np.loadtxt(const)
        layers = len(cons)        
        
    # processed data
    

    sys.stdout = StdoutRedirector(outputPanel)
    print ("> ")
    root.update()
    print ("> Stratification generator is being loaded...")
    root.update()
    print ("> -------------------------------------------------------------")
    root.update()
    print ("> Stratification Generator,     May 2022")
    root.update()  
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    
    print ("> Make sure that the following parameters are the")
    root.update() 
    print("> same displayed in the mdf file.")
    root.update()
    print ("> ")
    root.update()
    print ("> N = "+str(n))
    root.update()
    print ("> M = "+str(m))
    root.update()
    print ("> Layers ="+str(layers))
    root.update()    
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    
    if (n*m*layers>1000000):    
        print ("> This may take few minutes")
        root.update()  
        
    file_grd = open(folder_path+'/stratification.ini','w')

    for i in range(m):   # water level
        for j in range(n):
            file_grd.write("0")
            file_grd.write(' ') # (\t)  
        file_grd.write('\n')

    for k in range(layers):
        for i in range(m):  # u-velocity
            for j in range(0,n):
                file_grd.write("0")
                file_grd.write(' ') # (\t)  
            file_grd.write('\n')

    for k in range(layers):
        for i in range(m):  # v-velocity
            for j in range(n):
                file_grd.write("0")
                file_grd.write(' ') # (\t)  
            file_grd.write('\n')
    
    if son == 1:
        for k in range(layers):
            for i in range(m):  # salinity
                for j in range(n):
                    file_grd.write(str(sali[k]))
                    file_grd.write(' ') # (\t)  
                file_grd.write('\n')            
            
    if ton == 1:
        for k in range(layers):
            for i in range(m):  # temperature
                for j in range(n):
                    file_grd.write(str(temp[k]))
                    file_grd.write(' ') # (\t)  
                file_grd.write('\n')       

    if seon == 1:
        for k in range(layers):
            for i in range(m):  # secondary flow
                for j in range(n):
                    file_grd.write(str(seco[k]))
                    file_grd.write(' ') # (\t)  
                file_grd.write('\n')   

    if con == 1:
        for k in range(layers):
            for i in range(m):  # constitute 1
                for j in range(n):
                    file_grd.write(str(cons[k]))
                    file_grd.write(' ') # (\t)  
                file_grd.write('\n')   

    file_grd.close()
    
    
    num_data = son + ton + seon + con

    fig, ax = plt.subplots(figsize=(10,3),sharey=True)
    gs = gridspec.GridSpec(1,num_data)
    
    layers = np.arange(layers)
    
    for i in range(num_data):
        
        ax1 = plt.subplot(gs[0, 0])
        ax1.set_ylabel("Layers")
        if son == 1:
            ax1 = plt.subplot(gs[0, i])
            ax1.plot(sali,layers,lw=1,color='black')
            ax1.set_xlabel("Salinity (ppt)")
            continue
        if ton == 1:
            ax1 = plt.subplot(gs[0, i])
            ax1.plot(temp,layers,lw=1,color='black')
            ax1.set_xlabel("Temperature (oC)")
            continue
        if seon == 1:
            ax1 = plt.subplot(gs[0, i])
            ax1.plot(sali,layers,lw=1,color='black')
            ax1.set_xlabel("Secondary Flow (m/s)")
            continue
        if con == 1:
            ax1 = plt.subplot(gs[0, i])
            ax1.plot(cons,layers,lw=1,color='black')
            ax1.set_xlabel("Constituent (kg/m3)")
            continue
        
    plt.grid(True)
    fig.tight_layout()
    plt.savefig(folder_path+'/stratification.jpg',dpi=800)


    print ("> ")
    root.update()
    print ("> ----------------------------------------------------------")
    root.update() 
    print ("> ")
    root.update()
    print ("> FINISHED  Stratification Generator ")
    root.update() 
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    print ("> Check path for results:")
    root.update()
    print ("> "+folder_path)
    root.update() 
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    print ("> ")
    root.update()
    root.update()
    
    
    root.mainloop()
    sys.stdout = old_stdout