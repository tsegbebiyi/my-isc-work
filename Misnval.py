import numpy.ma as MA
import numpy as np

mar = MA.masked_array(range(10), fill_value = -999)
print mar
print mar.fill_value
mar[2] = MA.masked
print mar
print mar.mask
narr = MA.masked_where(mar < 7, mar)
print narr
print narr.fill_value
n = MA.filled(narr)
print n
print type(n)

#Part 2
m1 = MA.masked_array(range(1,9))
print m1
m2 = m1.reshape(2,4)
print m2
m3 = MA.masked_where(m2 > 6, m2)
print m3
m4 = m3 * 100
print m4
m5 = m3 - np.ones([2,4])
print m5
print type(m5)
