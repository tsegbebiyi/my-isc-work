import numpy as np
x = range (1,11)
print x
a1 = np.array(x, np.int32)
print a1.dtype
a2 = np.array(x, np.float32)
print a2.dtype

#creating arrays
x = np.zeros([2, 3, 4], np.int32)
print x
y = np.ones([2, 3, 4], np.int32)
print y
z = np.arange(0,1000,10,dtype=None)
print z
#help(np.arange)

#indexing and Slicing arrays
ar = np.array([2,3.2,5.5,-6.4,-2.2,2.4])
print ar[1]
print ar[1:4]

ar1 =np.array ([[2,3.2,5.5,-6.4,-2.2,2.4], 
     [1,22,4,0.1,5.3,-9], 
     [3,1,2.1,21,1.1,-2]])
print ar1[:, 3]
print ar1[1:4, 0:4]
print ar1[1:, 2]


