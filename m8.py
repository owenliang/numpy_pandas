import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x+1

plt.figure()
plt.plot(x,y)

ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0+1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[0, y0], color='black', linestyle='--')

# method 1
plt.annotate(r'$2x+1={}$'.format(y0), xy=(x0,y0), xycoords='data', fontsize=16,)

# method 2
plt.text(x0,y0+3, r'$hello\ world$', fontdict={'size':16, 'color':'r'})

plt.show()
