#Working on my the serial temperature data
from datetime import datetime, timedelta
def convert_time(tm):
	tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
	return tm
	
def convert_temp(temp):
	value = temp.strip("+").strip("C").lstrip("0")
	return float(value) + 273.15
	
infile = 'serial-temperature.tsv'
#infile 2 = 'serial-temperature.tsv'
outfile = 'Sensor-data.nc'
from csv import reader # import reader

#parse the data into python lists
times = []
temps = []

#open data and read into lists
with open(infile, 'rb') as tsvfile:
	tsvreader = reader(tsvfile, delimiter='\t')
	for row in tsvreader:
		times.append(convert_time(row[0]))
		temps.append(convert_temp(row[1]))



