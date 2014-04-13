def add(a,b):
	return a+b
def mul(a,b):
	return a*b
def sub(a,b):
	return a-b
def div(a,b):
	return a/b

a=int(raw_input("Enter first number:"))
b=int(raw_input("Enter second number:"))
x=raw_input("1.add\n2.mul\n3.sub\n4.div\nEnter your choice:")
if x=="1":
	print(add(a,b))
elif x=="2":
	print(mul(a,b))
elif x=="3":
	print(sub(a,b))
else:
	print(div(a,b))
