
# Import module for plotting 
###############################
#       Date : 5/1/2020       #
#       Author: Liam Lin      #
###############################

import matplotlib.pyplot as plt
import matplotlib.text as text 



days = range(0,22,3)
celcius_1 = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celcius_2 = [15.4, 13.1, 21.6, 18.1, 16.4, 20.5, 23.1, 13.2]

fig, ax = plt.subplots()


ax.plot(days, celcius_1,"o--b" ,label="Home")
ax.plot(days, celcius_2,"+-.r" ,label="Office")

ax.set_xlabel("Day")
ax.set_ylabel("Celcius")

axis_range = ax.axis()
msg = 'Axis Range: {0}'
msg = msg.format(axis_range)
print(msg)
#t = text.Text(16, 24, 'Text label', ha='left', va='bottom', axes=ax)
t = text.Text(4, 32, msg, ha='left', va='bottom', axes=ax)
ax.add_artist(t)


ax.set_title("Home and Office Temperature")
plt.grid(True)
plt.legend(loc="upper left")
plt.show()









#pl1 = plt.plot(days, celcius_1,"o--b" ,label="Home")
#pl2 = plt.plot(days, celcius_2, "+-.r",label="Office")
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#
#
#
#plt.legend(loc="upper left")             #Add legend option: 1: upper right
#plt.xlabel("Day")                #Add xlabel
#plt.ylabel("Celcius")            #Add ylabel
#plt.grid(True)
#plt.title("Home and Office Temperature")
#plt.show()

#fig, ax = plt.subplots()


#t = text.Text(16, 24, msg, ha='left', va='bottom', axes=ax)



