import matplotlib.pyplot as plt

# 窗口
plt.figure()

# 切割成2*2,绘制第1个小图
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)
plt.plot([0,1],[0,1])

plt.subplot(2,2,3)
plt.plot([0,1],[0,1])

plt.subplot(2,2,4)
plt.plot([0,1],[0,1])


# 窗口
plt.figure()

plt.subplot(2,1,1)  # 1行占用1格子开始的位置
plt.plot([0,1],[0,1])

# 2行占用4,5,6格子
plt.subplot(2,3,4)  
plt.plot([0,1],[0,1])

plt.subplot(2,3,5)
plt.plot([0,1],[0,1])

plt.subplot(2,3,6)
plt.plot([0,1],[0,1])

plt.show()
