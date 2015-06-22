import json
import clazz
import re
from pprint import pprint

childz=[]

def doohickey(jsonin):
	global childz
	try:
		jj=json.loads(str(jsonin))
		state=clazz.Statement(jj['_dname'],jj['_key'],jj['_raw'],jj['_child'],jj['_words'])
		for c in childz:
			print "1"
			state.addChild(c)
		return state
	except ValueError, e:
	#for jjj in jsonin:
	#	print jjj
		jjj=jj
		print jjj
		if jjj['_child']!=[]:
			app=(doohickey(jjj['_child']))
			print app
			childz.append(app)




	
f=open('keys.dat',"r")
ff=f.read()
j=(json.loads(ff))#,object_hook=as_statement_array))

buf=[]
for name,table_meta in j.iteritems():
	state=(doohickey(table_meta))
	state.setDescriptiveName(name)
	buf.append(state)
	childz=[]

for b in buf:
	if  b.getDescriptiveName()=="AquenticHaplorthods":
		for bb in (b.getChildren()):
			print bb['_raw']
		

