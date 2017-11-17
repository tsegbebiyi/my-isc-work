# Part 1
a = set([0,1,2,3,4,5])
b = set([2,4,6,8])
print a.union(b)
print a.intersection(b)

#Part 2
band = ["mel", "geri", "victoria", "mel", "emma"]
counts ={}
for name in band:
    #print name
    if name not in counts:
        counts[name] = 1
    elif name in counts:
        counts[name] +=1
    print name, counts[name] 
    
#Part 3           
if {"Temi":"Praise"}: 
    print 'hi'
else:
    print 'cool'    
    
d = {"maggie": "uk", "ronnie": "usa"} 
dir(d)
print dir(d)
x = d.items()
print x
y = d.keys()
print y
a = d.values()
print a
#b = d.get('maggie',nowhere) # this gives an error because the name maggie is already in the dictionary
#print b
b = d.get('ringo', 'nowhere')
print b
m = d.setdefault("Praise", "Peace")
print m
   


