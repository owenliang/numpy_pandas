import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
y1= (1-X/float(n))*np.random.uniform(0.5,1.0,n)
y2= (1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,y1,facecolor='#9999ff', label='a')
plt.bar(X,-y2,facecolor='#ff9999', label='b')
plt.legend()

for x,y in zip(X,y1):
    plt.text(x,y+0.05,'%.2f' % (y,), ha='center',va='bottom')

for x,y in zip(X,y2):
    plt.text(x,-y-0.05,'%.2f' % (y,), ha='center',va='top')
    
plt.show()
