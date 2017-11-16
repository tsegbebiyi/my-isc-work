import numpy as np
arr = np.array([range(4), range(10,14)])
print arr
print np.size(arr) # this can also be written as = arr.size()
print np.shape(arr)
print arr.max()
print arr.min()

#part 2
print arr.reshape(2,2,2)
print arr.transpose()
print arr.ravel()
print arr.astype(np.float32)
