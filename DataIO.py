#Open date weather.csv
#with open ('weather.csv','r') as reader:
 #   data=reader.read()
#print data

#READ data line by line
#with open ('weather.csv','r') as reader:
   # line=reader.readline()
    #total=0
    #count=0
    #while line :
        #print line
     #   line = reader.readline()

#print line

#Write rainfall data 
with open ('weather.csv','r') as reader:
    line=reader.readline()
    rain=[]
    for line in reader.readlines():
        cols = line.strip().split(",")
        print cols
        r = float(cols[-1])
        print r
        rain.append(r)

print rain
with open ('myrain.txt','w') as writer:
    for r in rain:
        writer.write(str(r) + "\n")


#advanced binary data writing 
import struct                        #import library
bin_data = struct.pack("bbbb", 123, 12, 45, 34)
with open ('mybinary.dat','wb') as bwriter:
    bwriter.write(bin_data)
with open ('mybinary.dat','rb') as breader:
    bin_data2 = breader.read()

data = struct.unpack("bbbb",bin_data2)
print data


#STRINGS
#PART 1
S = "I love to write python"
for i in S:
    print i

print S[4]
print S[-1]
print len(S)
print S[0]
print S[0][0] 
print S[0][0][0]

#part 2
S = "I love to write python"
split_s = S.split()
print split_s
   
for word in split_s:
 if word.find("i") > -1:
     print "I found 'i' in: '{0}'".format(word)
      
 if "i" in word:
     print "I found 'i' in: '{0}'".format(word)

#part 3
something="Completely Different"
print dir(something)
print type(something)
print something.count('t')
print something.find('plete')
print something.split('e')
thing2=something.replace('Different',"Silly")
print thing2
something[0] = "B"


