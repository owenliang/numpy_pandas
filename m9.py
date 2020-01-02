import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,20)
y = x*2+1

plt.figure()
plt.plot(x,y)

ax = plt.gca()
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox({'facecolor': 'green', 'edgecolor': 'black', 'alpha':0.7})
plt.show()
