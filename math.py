#Add Implementation
def add(x,y):
		return x+y
#Subtract Implementation
def subtract(x,y):
		return x-y			#on master branch
#Multiply Implementation
def multiply(x,y):
		return x*y		#on Bug456 branch
#Divide Implementation
def divide(x,y):
		if y==0:
			return DIVIDE_BY_0_ERROR
		else:
			return x/y		#on master branch

#Square Implementation
def square(x):
	return x*x