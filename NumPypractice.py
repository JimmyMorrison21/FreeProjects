import numpy as np

'''arr = np.array([1,2,3,4,5], dtype=np.int64)
print(arr)
arr1 = arr.astype(np.float32)
print(arr1)

a = np.array ([1,2,3])
b = np.array ([1,2,3])
c = a+b
print(c)'''


##Как поменять местами две строки в двумерном массиве NumPy? Поменяйте местами строки 1 и 3 массива a.#

#a = np.arange(24).reshape(3,8)
#b = np.array([(0,0,0),(0,0,0),(0,0,0)],dtype= np.int64)
#b[2],b[1],b[0] = a[0],a[1],a[2]
#print(b)
#print(a[[2,1,0],:])
#print(np.resize(a,(2,2)))
#print(a)
#b = np.arange(8).reshape(1,8)
#c = a*b
#print(c)
#print(np.delete(c,0,axis=0))
#c = np.array([(1,0.5,0.33),(0,1,0.33)],dtype=np.float32)
#print(np.sin(c))
#print(c.sum())
#x = np.abs(np.linspace(-2,2,5))[:,np.newaxis] + np.abs(np.linspace(-2,2,5))[np.newaxis,:]
#print((x == 2).astype(int) )
#print(x)
x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))
#print(xx)
#print(y)
#print(xx * y)
print(np.arange(0,100,1))