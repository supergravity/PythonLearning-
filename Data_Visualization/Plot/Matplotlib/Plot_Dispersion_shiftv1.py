# Import module for plotting 
###############################
#       Date : 5/8/2020       #
#       Author: Liam Lin      #
###############################

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.text as text

#### Input ####
print("Insert g value:")

g_ = float(input())

print("Insert Q_factor value:")

#gamma_ = float(input())
Q_factor = float(input())

fc = 6e9
gamma = fc / Q_factor



#print(type(g_))
#print(type(gamma_))


#### Define Function ####

def R(g,gamma,delta):
    #return ((pow(g,2))*(1/(x*gamma)))
    return g_**2 / delta / gamma

def k(g,gamma,x):
    return (x/x)


#### Plots ####



fx_name = r'$f(\Delta) = g^2$ Q $(\frac{1}{\Delta})$'

#delta=np.setdiff1d(np.linspace(0,50,100),[0]) #to remove the zero
delta=np.setdiff1d(np.linspace(100e6,1e9,1000),[0]) #to remove the zero
y=R(g_,gamma,delta)
#z=f(50E6,1E4,delta)
#r=k(1,1,delta)

fig, ax = plt.subplots()
ax.plot(delta/g_,y,"--b",label=fx_name)
#ax.plot(delta,z,"-.r",label="g =  ,Q_factor = ")
#ax.plot(delta,r,label="g = 1 , gamma = 1")
plt.axhline(1,color='k',label="R = 1")
plt.axvline(10,color='m',label='delta/g = 10')

ax.set_xlabel(r'$\Delta(g)$')
#ax.set_ylabel(r'$\frac{\chi}{\Gamma}$')
#ax.set_ylabel(r'$\chi$Q_factor')
ax.set_ylabel(r'Readability')
#ax.set_title(r'$\frac{\chi}{\Gamma} - g $')
plt.xlim(10,max(delta)/g_)
#plt.ylim(1,10)
ax.set_title(r'Readability - detuning')
plt.legend(loc="upper right")

plt.show()




