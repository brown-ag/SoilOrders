import json
import clazz
import re
from pprint import pprint

childz=[]
flah=""

def doohickey(jsonin):
#	global childz
#	global flah
	jj=jsonin
#	flag=False	
	try:
		state=clazz.Statement(jj['_dname'],jj['_key'],jj['_raw'],jj['_child'],jj['_words'])	
#		flag=True	
	except:
		jj=json.loads(str(jsonin))		
		#print len(jj)
		state=clazz.Statement(jj['_dname'],jj['_key'],jj['_raw'],jj['_child'],jj['_words'])
	if jj['_child']!=[]:
		for jjj in jj['_child']:
			#`print jjj
			if isinstance(jjj, clazz.Statement):
				#state.addChild(jjj)
				childz.append(jjj)
#				flag=True
			else:
				app=(doohickey(jjj))
				if isinstance(app, clazz.Statement):
					#state.addChild(app)
					childz.append(app)	
#					flag=True
				else:
					print(type(app))
#	else:
#		flag=True

#	if flag:
	return state
#	else:	
#		return None

f=open('keys.dat',"r")
ff=f.read()
j=(json.loads(ff))#,object_hook=as_statement_array))

buff=[]
for name,table_meta in j.iteritems():
	state=doohickey(table_meta)
	#print state
	state.setDescriptiveName(name)
	#print len(childz)	
	state.clearChildren()
	for c in childz:
		if isinstance(c, clazz.Statement):
		#	print(str(type(c)))
		#print state
			state.addChild(c)
#			print state.getChildren()
	childz=[]
	#print type(state)
	buff.append(state)

#print type(buf[1000].getChildren()[1])
for b in buff:
	#if  b.getDescriptiveName()=="AquenticHaplorthods":
	if b.getChildCount() > 0:
		print b.getDescriptiveName()
		print type(b)
		print b.getChildren()
		for bb in b.getChildren():
			#print type(bb)

			if bb.getChildCount() > 0:
				print bb.getChildren()	
		#	for bbb in bb.getChildren():
			#		print bbb.getText()	
			#else:
			#	print "\t"+bb.getText()	
