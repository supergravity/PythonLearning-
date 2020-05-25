import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.set()
sns.pointplot(x="sex", y="total_bill", hue="day", data=df)
plt.show()


