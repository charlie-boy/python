class first:
        def setname(self,value):
                self.name=value
        def display(self):
                print self.name
class second(first):
        def display(self):
                print "current value is:%s"%self.name
x=first()
y=second()

x.setname("ghh, ghgjghjghfvj")
y.setname("1234")
    
x.display()
y.display()

