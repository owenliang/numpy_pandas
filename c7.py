import numpy as np

a = np.arange(3,15)
print(a)
print(a[3])


b = a.reshape((3,4))
print(b)
print(b[2])
print(b[1][1])
print(b[2,1])
print(b[:,1])

for row in b:
    print(row)
for col in b.T:
    print(col)
print(np.array(b.flat))
print(b.flatten())
for item in b.flatten():
    print(item)


