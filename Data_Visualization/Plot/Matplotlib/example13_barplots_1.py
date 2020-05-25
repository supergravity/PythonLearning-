# Import module for plotting 
###############################
#       Date : 5/1/2020       #
#       Author: Liam Lin      #
###############################

import pandas as pd
import matplotlib.pyplot as plt

## LoadData

df = pd.read_csv("./FT748/Ch13/GSW_players_stats_2017_18.csv")
df_grouped =df.groupby("Pos")
position = df_grouped["Pos"].count()

## Plots

plt.bar([1,2,3,4,5],position)
plt.xticks([1,2,3,4,5],position.index)
plt.ylabel("Number of People")
plt.xlabel("Position")
plt.title("NBA Golden State Warriors")
plt.show()



