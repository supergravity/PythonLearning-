# Import module for plotting 
###############################
#       Date : 8/10/2020       #
#       Author: Liam Lin      #
###############################

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.text as text
import math  

#### Define Parameters ####

d   = 8e-4  #The distance between two slits
L   = 0.8   #The distance between the slits and the screen
lam = 6.4e-7  #The wavelength of the monochromatic light 
f   = 500             #The frequency of how phase shifts from 0 to 2pi
#t   = np.linspace(0,1,100)#The time duration 
t_1   = 1e-3 
t_2   = (1/5e2) 
t_3   = (1/2.5e2) 

n   = np.linspace(-2,2,5)

Xn  = (L*lam*n/d)*1e3 
Xn_1 = Xn + (L*lam/d)*f*t_1*1e3 
Xn_2 = Xn + (L*lam/d)*t_2*1e3
Xn_3 = Xn + (L*lam/d)*t_3*1e3
Yn  = np.linspace(0,0,5)

print(f*t_1)
print(f*t_3)

fig, ax = plt.subplots()
ax.plot(Xn,Yn,"ob")
ax.plot(Xn_1,Yn,"or")
ax.plot(Xn_2,Yn,"og")
ax.plot(Xn_3,Yn,"ok")

plt.show()


