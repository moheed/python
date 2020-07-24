from abc import ABC, abstractmethod 
"""
Python comes with a module which provides the base for defining Abstract Base classes(ABC) 
and that module name is ABC. ABC works by decorating methods of the base class as abstract and 
then registering concrete classes as implementations of the abstract base. 
A method becomes abstract when decorated with the keyword @abstractmethod.

"""
# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 

class Polygon(ABC): 

	# abstract method 
	def noofsides(self): 
		pass

class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 

class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 

class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 

class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 

# Driver code 
R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 

"""
Its more of a factory-method, where the base-class (factory) defines abstract-methods
which must be implemented by derived classes from the factory.
@abc.abstractproperty
@abstractmethod
Concrete classes contain only concrete (normal)methods whereas abstract classes 
may contains both concrete methods and abstract methods.
"""


"""
Why use Abstract Base Classes :
By defining an abstract base class, you can define a common Application Program Interface(API)
 for a set of subclasses. This capability is especially useful in situations where a third-party 
 is going to provide implementations, such as with plugins, but can also help you when working in
 a large team or with a large code-base where keeping all classes in your mind is difficult or not possible.
"""
"""
A method becomes abstract when decorated with the keyword @abstractmethod. 
"""
