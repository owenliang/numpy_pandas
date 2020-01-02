import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5))
l1, = plt.plot(x,y2, label='up')
l2, = plt.plot(x,y1, label='down', color='red', linewidth=1.0, linestyle='--')
plt.legend(handles=[l2], labels=['aaa',], loc='upper right')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks=np.linspace(-1,2,5)
#print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],['really bad', 'bad', 'normal', 'good'])
plt.show()
