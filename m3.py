import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x+1
y = x**2
plt.plot(x,y)
plt.show()
