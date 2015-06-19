import re
import clazz
tex=open("keysout.html","r")
lines=tex.readlines()
tex.close()
keys={}
name=""
start=-1
stop=-1
mode=0
i=0
lnest=-1
childcount=0
for l in lines:
	if mode == 0:
		m21=re.search("</br>(\w{4,}[^\.\)].*)",l)
#`		print(l)
		if m21 != None:
		#	print(m21.group(1))
			name=m21.group(1)
			start=i
			mode=1
			lnest=-1
			childcount=-1
			if(m21.group(1)=="Typic Haploxererts"):
				break
	elif mode == 1:
		if lnest==-1:
			m23=re.search("<i>(.*?)</i>(.*?):",l)
			if m23 != None:
				print m23.groups( #NB; CHECK FOR ANOTHER SET OF TAGS IN GROUP 2)
		nest=l.count(" - \t")
		if nest>0: 
			childcount+=1
			lnest=nest		
			print nest
	m22=re.search("</br>---",l)
	if m22 != None:
		stop=i	
		mode=0	
	i+=1
	if childcount > 0:
		print(str(childcount)+" children")

