from json import JSONEncoder
from json import JSONDecoder
import re
import clazz

class StatementEncoder(JSONEncoder):
	def default(self, obj):
		if hasattr(obj,'_child'):
			for o in obj._child:
				obj.__dict__['_child'].append(default(o))
		return obj.__dict__

class StatementDecoder(JSONDecoder):
	def default(self, obj):
		if '_raw' in obj:	
			state=clazz.Statement(obj['_dname'],obj['_key'],obj['_raw'],obj['_child'],obj['_words'])
			print state.getDescriptiveName()
			print len(state.getChildren())
			return state

class Statement(object):
		
	def __init__(self,dname,key="",raw="",child="",words=""):
		self.setDescriptiveName(dname)	
		self._words=words
		self._child=child
		self._raw=raw
		self._dname=dname
		self._key=key
	
	def setKey(self, k):
		self._key=k
	
	def getKey(self):
		return self._key

	def setDescriptiveName(self,dn):
		self._dname=dn
	
	def getDescriptiveName(self):
		return self._dname
	
	def getChildCount(self):
		return len(self._child)	

	def setText(self,text):
		#self.words=re.compile("\W+",re.UNICODE).split(text)		
		self._raw=text

	def getText(self):
		return self._raw
	
	def getWords(self):
		return self._words

	def getChildren(self):	
		return self._child

	def addChild(self,ch):
		if(isinstance(ch,Statement)):
			self._child.append(ch)
		
