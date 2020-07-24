# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:30:16 2020
A <--> B
Va = d[B]/dt = ka[A]
Vb = d[A]/dt = kb[B]
Ctot = [A]+[B]
@author: chris
"""

import os
import matplotlib.pyplot as plt
import numpy as np

t_tot = 100    #CHANGE THIS, time of the symulation
dt = 0.01          #CHANGE THIS, time incremental step
ka = 0.20      #CHANGE THIS, M/step
kb = 0.05          #CHANGE THIS, M/step
Ca0 = 1000      #CHANGE THIS, initial concentration of specie A
Cb0 = 0          #CHANGE THIS, initial concentration of specie B

Ctot = Ca0 + Cb0

def symulation():
    
    Ca = Ca0
    Cb = Cb0
    t_array = []
    Ca_array = []
    Cb_array = []
    

    pathCWD = os.getcwd()
    pathSym = pathCWD + "\\Symulator_all_species\\symulation_AB.txt"
    s = open(pathSym,"w+")
    #save in test file first line
    s.write("Time" + "   " + "[A]" + "   " + "[B] \n")
    
    t=0    
    while t <= t_tot:
        t_array.append(round(t,3))
        Ca_array.append(round(Ca,2))
        Cb_array.append(round(Cb,2))
        s.write(str(round(t,3)) + " " + str(round(Ca,2)) + " " + str(round(Cb,2)) + "\n")
        Cb = Ctot - Ca
        Cb = A_reaction(Ca, Cb)
        Ca = Ctot - Cb
        Ca = B_reaction(Ca, Cb) 
        t = t+dt

        #save in text file
        
    s.close()

    plt.plot(np.array(t_array), np.array(Ca_array),  label='[A]')
    plt.plot(np.array(t_array), np.array(Cb_array),  label='[B]')
    plt.title('A <--> B')
    plt.ylabel('[X]')
    plt.xlabel('time')
    plt.legend()
    plt.show()



def A_reaction(Ca, Cb):
    
    Cb = Cb + ka*Ca*dt
    
    return Cb


def B_reaction(Ca, Cb):
    
    Ca = Ca + kb*Cb*dt
    
    return Ca


symulation ()
