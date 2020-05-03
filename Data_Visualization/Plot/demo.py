import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Generating time scale 

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()

## Generating 3 sets of data, each with 200 Normal Distribution

y = np.random.randn(200, 3).cumsum(0)
plt.plot(x, y)
plots = plt.plot(x, y)
plt.legend(plots, ('Apple', 'Facebook', 'Google'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})
plt.show()






