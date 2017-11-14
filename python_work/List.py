#Exercise Part 1
#mylist=[1, 2, 3, 4, 5]
#print mylist
#print mylist[1]
#print mylist[3]
#print mylist[0:4]
#print mylist[1:4]

#Exercise Part 2
#x=range(1,11)
#print x
#x[0]=10
#print x[0]
#x.insert(12,11)
#print x
#x.extend([12,13, 14])
#print x

#Exercise Part 3
forward=[]
backward=[]
values=["a", "b", "c"]
for i in values:
    forward.append(i)
    backward.insert(0,i)
    
print forward, backward
forward.reverse()
print forward, backward
