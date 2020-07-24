# -*- coding: utf-8 -*-

"""
Created on Wed Jul 22 21:30:16 2020
HA <--> H+ + A-
Vha = d[A-]/dt = ka[HA]
Vh = d[HA]/dt = kb[H+][B]
Ctot = [HA]+[A-]
@author: chris
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import math

t_tot = 1000    #CHANGE THIS, time of the symulation
dt = 0.1          #CHANGE THIS, time incremental step
ka = 0.01      #CHANGE THIS, M/step
kb = 0.00001          #CHANGE THIS, M/step
C_HA_0 = 1       #CHANGE THIS, initial concentration of specie HA
C_A_0 = 0.2          #CHANGE THIS, initial concentration of specie a-
C_H_0 = 0.0001          #CHANGE THIS, initial concentration of specie H+

C_A_tot = C_HA_0 + C_A_0
C_H_tot = C_HA_0 + C_H_0

def symulation():
    
    C_HA = C_HA_0
    C_A = C_A_0
    C_H = C_H_0
    t_array = []
    C_HA_array = []
    C_A_array = []
    C_H_array =[]
    pH_array = []
    

    pathCWD = os.getcwd()
    pathSym = pathCWD + "\\Symulator_all_species\\symulation_HA.txt"
    s = open(pathSym,"w+")
    #save in test file first line
    s.write("Time" + "   " + "[HA]" + "   " + "[A-]" + "[H+] \n")
    
    t=0    
    while t <= t_tot:
        t_array.append(round(t,3))
        C_HA_array.append(round(C_HA,2))
        C_A_array.append(round(C_A,2))
        C_H_array.append(round(C_H,2))
        pH_array.append(round(-math.log10(C_H),2))
        s.write(str(round(t,3)) + " " + str(round(C_HA,2)) + " " + str(round(C_A,2)) + " " + str(round(C_H,2))+"\n")
        C_A = C_A_tot - C_HA
        C_H = C_H_tot - C_HA
        [C_A, C_H] = A_reaction(C_HA, C_A, C_H)
        C_HA = C_A_tot - C_A
        C_H = C_H_tot - C_HA
        C_HA = B_reaction(C_HA, C_A, C_H) 
        t = t+dt

        #save in text file
        
    s.close()
    plt.subplot(2, 1, 1)
    plt.plot(np.array(t_array), np.array(C_HA_array),  label='[HA]')
    plt.plot(np.array(t_array), np.array(C_A_array),  label='[A-]')
    plt.plot(np.array(t_array), np.array(C_H_array),  label='[H+]')
    plt.title('A <--> B')
    plt.ylabel('[X]')
    plt.xlabel('time')
    plt.legend()
    plt.show()
 
    plt.subplot(2, 1, 2)
    plt.plot(np.array(t_array), np.array(pH_array),  label='pH')
    plt.title('A <--> B')
    plt.ylabel('pH')
    plt.xlabel('time')
    plt.legend()
    plt.show()



def A_reaction(C_HA, C_A, C_H):
    
    C_A = C_A + ka*C_HA*dt
    C_H = C_H + ka*C_HA*dt
    
    return C_A, C_H


def B_reaction(C_HA, C_A, C_H):
    
    C_HA = C_HA + kb*C_A*C_H*dt
    
    return C_HA


symulation ()