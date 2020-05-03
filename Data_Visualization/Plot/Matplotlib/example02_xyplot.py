# Import module for plotting 
###############################
#       Date : 5/1/2020       #
#       Author: Liam Lin      #
###############################

import matplotlib.pyplot as plt

days = range(0,22,3)
celcius_1 = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celcius_2 = [15.4, 13.1, 21.6, 18.1, 16.4, 20.5, 23.1, 13.2]

############### Make Plot ###############

#Plot Style
#plt.style.use("ggplot")              #Add style
#plt.style.use("bmh")              #Add style
#plt.style.use("seaborn")              #Add style



#plt.figure(figsize=(8, 6))      #Adjust the size of the figure in the unit of inch
#plt.plot(days, celcius_1,"o--b" ,days, celcius_2, "+-.r")
plt.plot(days, celcius_1,"o--b" ,label="Home")
plt.plot(days, celcius_2, "+-.r",label="Office")
legend_1 = plt.legend(loc="upper left")             #Add legend option: 1: upper right
plt.xlabel("Day")                #Add xlabel
plt.ylabel("Celcius")            #Add ylabel
plt.title("Home and Office Temperature") #Add title
plt.grid()                       #Add Grid on the plot

from matplotlib.legend import Legend 


print("Axis Range: ",plt.axis())
#legend_2 = plt.legend("Axis Range: %s" %plt.axis())
#axis_range = plt.axis()
#msg = 'Axis Range: {0}'
#msg = msg.format(axis_range)
#legend_2 = plt.legend(msg)
#plt.axes.add_artist(legend_1)
#plt.axes.add_artist(legend_2)

plt.show()


