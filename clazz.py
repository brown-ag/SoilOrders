import re

class Statement:
	words=[]
	child = []
	levels=[]
	level=-1

	def __init__(self,text,l):
		self.level=l
		self.words=re.compile("\W+",re.UNICODE).split(text)		
	
	def getWords():
		return self.words

	def getChildren(lvls):	
		return self.child[lvls]

	def addChild(ch,l):
		if(isinstance(ch,Statement)):
			child.append(ch)
			ch_levels.append(l)


		
