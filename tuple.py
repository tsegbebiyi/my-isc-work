t=[1]
print t[-1]

l=range(100,201)
tu = tuple(l)
print tu[0], tu[-1]

mylist=[23, "hi" , 2.4e-10]
#for (i, name) in enumerate(mylist): Same as the last two lines
 #   print i, name
for (count, item) in enumerate(mylist):
    print count, item
   
first, middle, last = mylist
(first, middle, last) = (middle, last, first)
print "first", "middle", "last"
