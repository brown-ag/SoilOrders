from json import JSONEncoder
import re
import clazz
import sys
class StatementEncoder(JSONEncoder):

	def default(self, obj):
		#if hasattr(obj,'_child'):	
		#	if(obj._child != []):
		#		for o in obj._child:
		#			if obj==o: break	
		#			obj.__dict__['_child'].append(self.default(o))
		if isinstance(obj, clazz.Statement):
			return obj.__dict__
		return obj

class Statement(object):
		
	def __init__(self,dname):#,key="",raw="",child=[],words=[]):
		self.setDescriptiveName(dname)	
		self._words=[]
		self._child=[]
		self._raw=""
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
		if(not hasattr(self,"_child")):
			self._child=[]
		if(isinstance(ch,Statement)):
			#print type(ch)
			self._child.append(ch)
	def clearChildren(self):
		self._child=[]
