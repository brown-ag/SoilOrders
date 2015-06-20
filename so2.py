import json
import re
import clazz
tex=open("keysout.html","r")
lines=tex.readlines()
tex.close()
keys={}
jkeys={}
keysid=""
name=""
start=-1
stop=-1
mode=0
i=0
lnest=0
childcount=0
buff = ""

def print2(what):
	global buff
	buff+=str(what)+"\n"
	print what

done=False
maxc=0
best=""
sbase={}
liter=lines.__iter__()
for l in liter:
	dname=""
	if mode == 0:
		m21=re.search("</br>(\w{4,}[^\.\)].*)",l)
#		print(l)
		if m21 != None:
			print2(m21.group(1))
			name=m21.group(1)
			start=i
			mode=1
			lnest=0
			childcount=0
			dname=re.sub("\s","",name)

			sbase[dname]=clazz.Statement(dname)
			
			if(m21.group(1)=="Typic Haploxererts"):
				done=True
				#break
	if mode == 1:
		sparent=sbase[dname]
		lastparent=""
	 	lastlastparent=""
		#print start	
		k = 0
		ll=l
		lastline=l
		while(True):
			print2(sparent.getChildCount())
			if lnest==0:
				m2=re.search(">([A-Z]{0,4})\.\s\s",ll)
				#m23=re.findall("i>(.*?)</i>.*",l)
				#for mm in m23:
				#	if mm != None:
				#		print2(mm)
				if m2 != None:
					sparent.setText(ll)
					keysid= m2.group(1)
					sparent.setKey(keysid)
			m23=re.search("<i>(.*?)</i>(.*?):?",ll)
			if m23 != None:
				print2(m23.group(1))
				print2(m23.group(2))
			nest=ll.count(" - \t")
			lnest=nest
			if nest>0: 
				#print nest
				print2(str(nest)+':'+str(lnest))
				if nest > lnest:
					if sparent != "":
						lastlastparent=lastparent
						lastparent=sparent
					sparent=clazz.Statement(dname+"."+str(i)+"."+str(lnest)+"."+str(k-1))
					sparent.setText(lastline)
				elif nest < lnest:
					#add sparent onto sbase
					sbase[dname].addChild(sparent)
					sparent=lastparent
					lastparent=lastlastparent
				if sparent != "":
					sbuf=clazz.Statement(dname+"."+str(i)+"."+str(nest)+"."+str(k))
					sbuf.setText(ll)
					sparent.addChild(sbuf)
					childcount+=1
			else:
				m22=re.search("</br>---",ll)
				if m22 != None:
					stop=i	
					keys[dname]=sbase[dname]
					jkeys[dname]=clazz.StatementEncoder().encode(sbase[dname])
					if childcount >= maxc:
						maxc=childcount
						best=dname
					print2(str(childcount)+" children")
					mode=0
					k+=1
					break
			lastline=ll					

			m24=re.search(";<i>(.{2,}?)</i>",ll)			
			if m24 != None:
				print2(m24.group(1)) #TODO: CHECK FOR ANOTHER SET OF TAGS IN GROUP 2)
			lastline=ll
			ll=liter.next()	
			k+=1

	if done: 
		break
	i+=1
print maxc
print best
#print(keys)
json.dump(jkeys,open("keys.dat",'w'))
#out=open("childmap.txt","w")
#out.write(buff)
#out.close()
#
#for nom,state in keys.iteritems():
#	print nom
state=keys['CHAPTER12']
#TODO: HANDLING FOR MULTIPAGE TAXA:
print state.getKey()
print state.getText()
print state.getChildren()
for c in (state.getChildren()).__iter__():
	ch=c.getChildren()
	if(c.getChildCount() > 0):
		print c.getChildren()
		for chh in ch.__iter__():
			if(chh.getChildCount()>0):
				print chh.getChildren();
