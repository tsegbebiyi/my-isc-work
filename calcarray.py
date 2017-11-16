import numpy as np
a = np.array([range(4), range(10,14)])
b = np.array ([2,-1,1, 0])
#print a , b
ab = a * b
print ab
b1 = b * 100
b2 = b * 100.0
print b1 , b2
b3 = b1 == b2
print b3
print b1.dtype , b2.dtype

#Array comparison
arr = np.arange(10)
a = arr < 3
print a
a1 = np.less(arr, 3)
print a1
condition = np.logical_or(arr < 3, arr > 8)
b = np.where(condition, arr * 2, arr * 9)
print b

#mathematical function
def calcwind (u,v, minmag = 0.1):
    mag = ((u**2) + (v**2))**0.5
    r = np.where(mag > minmag, mag, minmag)
    return r
    
u = np.array
