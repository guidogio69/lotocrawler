##http://www.loteriadesalta.com/loteria-ws/api/extracto/CHANGUITA/01-10-2015
##http://www.loteriadesalta.com/loteria-ws/api/extracto/QUINIELA_SALTA/ultimo?_=1449445530104
##http://www.loteriadesalta.com/loteria-ws/api/extracto/QUINIELA_SALTA/06-12-2015


#!/usr/bin/python

import urllib
from datetime import timedelta, date
import time

##esto me parece esta al pedo
##sopa = urllib.urlopen('http://www.loteriadesalta.com/loteria-ws/api/extracto/CHANGUITA/01-10-2015').read()

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def creartxt():
	archi=open('changuita-'+fecha,'w')
	archi.close()

def grabartxt():
	archi=open('changuita-'+fecha,'a')
	archi.write(sopa)
	archi.close()
#Fecha inicio y fin crawleo
start_date = date(2015, 1, 1)
end_date = date(2015, 12, 1)
	
for single_date in daterange(start_date, end_date):
	fecha = single_date.strftime("%d-%m-%Y")
	sopa = urllib.urlopen('http://www.loteriadesalta.com/loteria-ws/api/extracto/CHANGUITA/'+fecha).read()
	time.sleep(5)
	creartxt()
	grabartxt()

print "Listortiiiiiii"
