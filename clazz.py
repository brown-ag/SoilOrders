from json import JSONEncoder
import re
class StatementEncoder(JSONEncoder):
	def default(self, obj):
		#print obj
		if hasattr(obj,'child'):
			buf=[]
			for o in obj.child:
				buf.append(o.__dict__)
			#return buf
		return obj.__dict__

class Statement(object):
		
	def __init__(self,dname):
		self.setDescriptiveName(dname)	
		self._words=[]
		self._child=[]
		self._raw=""
		self._dname=""
		self._key=""

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
		
