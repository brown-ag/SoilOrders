#from sys import argv
#script, filename = argv
import re

filename="keys.xml"
txt = open(filename)
i=0
mode=0
#lines=txt.readlines()
for l in txt:
	i=i+1
	if mode==0:
		m1=re.search('font=\"3\">([A-Z]{1,4})\.\s\s?(.*)<',l)
		if m1 != None:
			mode=1 #we are inside a taxonomic clause
			print m1.groups() 
			print i
	if mode==1:
		m2=re.search('font=\"8\"><b>(.*)</b>?(,\sp.\s(\d+))?<',l)
		if m2 != None:
			mode=0
			print m2.groups()
			print i
			print "--------------------------"


