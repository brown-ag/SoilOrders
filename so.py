#from sys import argv
#script, filename = argv
import re

buf=""

filename="keys.xml"
fileout="keysout.html"
txt = open(filename)
i=0
mode=-1
start=-1
end=-1
lines=txt.readlines()
txt.close()

def print2(what):
	global buf
	#print what
	buf+=''.join(what)
	buf+='\n'
	return

for l in lines:
	i=i+1
	m=None
	if mode == -1: m=re.search('<b>Key to Soil Orders</b>',l)
	if m != None: mode=0
	if mode==0:
		m1=re.search('\">([A-Z]{0,4})\.\s\s?.*<',l)
		if m1 != None:
			mode=1 #we are inside a taxonomic clause
			print2(m1.group(1)) 
			start=i
			#print i
	if mode==1:
		m2=re.search('font=\"\d+\"><b>(.{2,})</b>(?:,\sp.\s(\d+))?<',l)
		if m2 != None:
			mode=0
			print2("<TAXON>"+m2.group(1)+"</TAXON>")
			if m2.group(2) != None:
				print2(m2.group(2))
			end=i
			#prin i
			last=-1
			nest=0
			for ll in lines[(start-1):end]:
			  	#buf+=ll
				#buf+='\n'
				m3=re.search('<text\stop="\d{3,}"(?:.*)">(.*)</text>',ll)
				if m3 != None:
					m4=re.search('.([1-9a-z]).\s\s',m3.group(1))
					if m4 != None:
						bullet=m4.group(1)
						if bullet.isdigit()==True:
							toggle=0
						else:
							if bullet.isupper():
								toggle=1
							else:
								toggle=2	 
						if last!=toggle: nest+=1
						last=toggle
						print2('\n')
					print2((nest*'\t')+m3.group(1))
			#print2(buf)
			print2("--------------------------")
out=open(fileout,'w')
out.write(buf)
out.close()


