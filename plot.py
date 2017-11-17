import matplotlib.pyplot as plt
#plt.figure()
#x = range(10)
#plt.plot(x)
#plt.show()
#print 'hello'
#plt.clf()

#part 2
#plt.pause(1)
#Time = range(7)
#co2 = [250,265,272,260,300,320,389]
#plt.plot(Time,co2)
#plt.title('Co2 concentration with Time')
#plt.ylabel('Concentration(ppm)')
#plt.xlabel('Times (s)')
#plt.show()

#Part 3
#Time = range(7)
#co2 = [250,265,272,260,300,320,389]
#temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
##plt.plot(Time,co2, 'b---')
##Time, temp, 'r*---')
#plt.ylabel('Concentration(ppm)')
#plt.xlabel('Time (s)')
#plt.title('Co2 concentration and Temp with Time')
#plt.plot(Time, co2, 'b', label = "Co2")
#plt.plot(Time, temp, 'r--', label = "temp")
#plt.legend()
#plt.show()

#Part 4
#fig, ax1 = plt.subplots()
#Time = range(7)
#co2 = [250,265,272,260,300,320,389]
#Temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
#ax1.plot(Time,co2, 'b--')
#ax1.set_ylabel('[Co2]')
#ax2 = ax1.twinx()
#temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
#ax1.plot(Time,Temp, 'r*-')
#ax2.set_ylabel('Temp (degC)')
#plt.show()

#Part 5
plt.subplot(1,3,1)
x = range(0,10, 1)
plt.plot(x)
plt.subplot(1,3,2)
y = range (10,0, -1)
plt.plot(y)
plt.subplot(1,3,3)
z =[4] * 10
plt.plot(z)
plt.show()
