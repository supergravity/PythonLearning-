# Import module for plotting 
###############################
#       Date : 5/1/2020       #
#       Author: Liam Lin      #
###############################

import matplotlib.pyplot as plt

data = [-1, -4.3, 15, 21, 31]
#plt.plot(data)              # x axis is 0,1,2,3,4
#plt.plot(data,"o--b")       # draw options: o:circle marker --:dashed line style b:blue markers
plt.plot(data,"+-.r")        # draw options: +:plus   marker -.:dashed line style r:blue markers
plt.show()


