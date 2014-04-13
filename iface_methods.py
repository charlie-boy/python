class Fridge:

	self.items[foodname]=self.items[foodname]+quantity

	def add_one(self,foodname):
		if type(foodname)!=type(""):
			print "error"
		else:
			self.__add_multi(foodname,1)
		return True

	def add_many(self,fooddict):
		if type(fooddict)!=type({}):
			print "error"
		else:
			for item in fooddict.keys():
				self.__add_multi(item,fooddict[item])
		return
