#!/usr/bin/python2.7
from datetime import datetime
import serial
ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=9600,
   bytesize=serial.EIGHTBITS,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE)
   
#2 print temperature 
#print ser.read(size = 8)

#3 print date with temp data
print datetime.utcnow().isoformat(),ser.read(size=8)

#4 compare with #3
#datastring	=	ser.read(size=8)
#print	datetime.utcnow().isoformat(),	datastring
#ser.close()

#5 Loop over 4
#while ser.isOpen():
#    datastring	=	ser.read(size=8)
#    print	datetime.utcnow().isoformat(),	datastring

'''#6 readline
#!/usr/bin/python2.7
from	datetime	import	datetime
import	serial,	io
ser	=	serial.Serial(
			port='/dev/ttyUSB0',
			baudrate=9600,)
			
sio	= io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')
while	ser.isOpen():
			datastring	=	sio.readline()
			print	datetime.utcnow().isoformat(),	datastring
ser.close() '''

#7 writing the logged data
#!/usr/bin/python
'''This	version	of	the	readserial	program	demonstrates
using	python	to	write	an	output	file'''
from	datetime	import	datetime
import time #to help import time
import	serial,	io
outfile='/tmp/serial-temperature.tsv'
ser	=	serial.Serial(
			port='/dev/ttyUSB0',
			baudrate=9600,
)
sio	=	io.TextIOWrapper(
			io.BufferedRWPair(ser,	ser,	1),
			encoding='ascii',	newline='\r'
)
with open(outfile,'a')	as	f:	#appends	to	existing	file
    while	ser.isOpen():
	    time.sleep(60) # to help read temp every 60s
	    datastring	=	sio.readline()
	    #\t	is	tab;	\n	is	line	separator
	    f.write(datetime.utcnow().isoformat()	+	'\t'	+	datastring	+	'\n')
	    f.flush()	#included	to	force	the	system	to	write	to	disk
ser.close()


