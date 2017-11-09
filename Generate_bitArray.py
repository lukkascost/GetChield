from datetime import datetime
from lib.Devices import bluetooth
from lib.Geometrics.Circle import * 
from Classes import *

date = datetime.now()
d1  = 10
d2  = 2
d3  = 11
angulo = 290

print date

year = date.year/100
year = year*100
year = date.year - year
print year


day =       "{0:05b}".format(date.day)
month =     "{0:04b}".format(date.month)
year =      "{0:07b}".format(year)
hour =      "{0:05b}".format(date.hour)
minute =    "{0:06b}".format(date.minute)
distance1 = "{0:04b}".format(d1)
distance2 = "{0:04b}".format(d2)
distance3 = "{0:04b}".format(d3)
angle =     "{0:09b}".format(angulo)


stringBit =  day+month+year+hour+minute+distance1+distance2+distance3+angle
print stringBit
print day,month,year,hour,minute,distance1,distance2,distance3,angle
print hex(int(stringBit,2))[-12:].upper()



