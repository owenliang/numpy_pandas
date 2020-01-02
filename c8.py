import numpy as np

a = np.array([1,1,1,])
b = np.array([2,2,2])

c  = np.vstack((a,b))
print(a.shape, c.shape)

d = np.hstack((a,b))
print(d)
print(d.shape)

print(a.T)

e = a[:, np.newaxis]
f = b[:, np.newaxis]
print(e)
print(f)
print(np.vstack((e,f)))

g = np.concatenate((e,f), axis=0)
print(g)
