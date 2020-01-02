from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig =plt.figure()
ax = Axes3D(fig)

X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)

# 画图
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
# 画等高线
ax.contourf(X,Y,Z,zdir='x',offset=-2,cmap='rainbow')
ax.set_zlim(-2,2)

plt.show()
