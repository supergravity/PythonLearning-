# Import module for plotting 
###############################
#       Date : 5/1/2020       #
#       Author: Liam Lin      #
###############################

import matplotlib.pyplot as plt
import matplotlib.text as text

days = range(1,9)
celcius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celcius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]

fig, ax = plt.subplots()

ax.plot(days, celcius_min,"o--b" ,label="celcius min")
ax.plot(days, celcius_max,"+-.r" ,label="celcius max")

ax.set_xlabel("Day")
ax.set_ylabel("Celcius")

#plt.axis([0,10,15,40])
plt.xlim(0,10)
plt.ylim(15,40)
axis_range = ax.axis()
msg = 'Axis Range: {0}'
msg = msg.format(axis_range)
print(msg)
#t = text.Text(16, 24, 'Text label', ha='left', va='bottom', axes=ax)
t = text.Text(1, 32, msg, ha='left', va='bottom', axes=ax)
ax.add_artist(t)

ax.set_title("min and max Temperature")
plt.grid(True)
plt.legend(loc="upper left")
plt.savefig("Figure_ex03_1.png")
#plt.savefig("Figure_ex03_1.svg")
#plt.savefig("Figure_ex03_1.pdf")
plt.show()




