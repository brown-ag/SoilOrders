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
	#buf+='</br>\n'
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
			#print2(m1.group(1)) 
			start=i
			#print i
	if mode==1:
		m2=re.search('font=\"\d+\"><b>(.{2,})</b>(?:,\sp.\s(\d+))?<',l)
		if m2 != None:
			mode=0
			#print2("<TAXON>"+m2.group(1)+"</TAXON>")
			#if m2.group(2) != None:
			#	print2(m2.group(2))
			end=i
			nest=1
			last=-1
			
			print2(m2.group(1)+'\n</br>')
			for ll in lines[(start-1):end-1]:
			  	#buf+=ll
				#buf+='\n'
				m3=re.search('<text\stop="\d{3,}"(?:.*)">(.*)</text>',ll)
				if m3 != None:
					slab=m3.group(1)
					m4=re.search('([1-9a-z][\)\.])\s\s',slab)
					if m4 != None:
						bullet=m4.group(1)
						#print2(bullet)
						if(bullet.endswith('.')):
							if(bullet[:1].isdigit()):
								nest=2
							else:
								if(bullet[:1].isupper()):
									nest=1
								else:
									nest=3
						else:
							if(bullet[:1].isdigit()):
								nest=4
							else:
								nest=5
						print2('\n</br>')
						last=nest
						slab=((nest*' - \t')+m3.group(1))
					addCR = False
					if(len(slab)>10):
						addCR=False
					else:
						if re.search('<b>.</b>',slab) != None:
							slab=""
					print2(slab)
					if(addCR): print2('</br>\n')
			print2("\n</br>--------------------------\n</br>")
out=open(fileout,'w')
out.write(buf)
out.close()


