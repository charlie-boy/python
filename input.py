class firstclass:
    def function(self, value):
        self.a = value

    def display(self):
        print self.a

class secondclass(firstclass):
    def display(self):
        print "current value: '%s'" %self.a

x=firstclass()
y=secondclass()
x.function("The boy called Brian")
y.function(42)
x.display()
y.display()
alsamixer
