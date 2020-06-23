# Python Program to depict multiple inheritance 
# when method is overridden in both classes 

"""
In the case of multiple inheritance a given attribute is first searched in the current class 
if it’s not found then it’s searched in the parent classes. 
The parent classes are searched in a depth-first, left-right fashion and each class is searched once.
One can see Method Resolution order by:
Class4.mro()
or class4.__mro__
"""

class Class1: 
	def m(self): 
		print("In Class1") 
		
class Class2(Class1): 
	def m(self): 
		print("In Class2") 

class Class3(Class1): 
	def m(self): 
		print("In Class3") 
		
class Class4(Class2, Class3): 
	pass
	
obj = Class4() 
obj.m() 
#oupute will: method() of class2, then method of class3
