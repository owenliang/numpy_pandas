import matplotlib.pyplot as plt
import numpy as np

a=np.random.random(9).reshape(3,3)
plt.imshow(a,interpolation='nearest',)  # 绘图
plt.colorbar(shrink=.9)
plt.show()
