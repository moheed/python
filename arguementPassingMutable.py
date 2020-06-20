print("Hello World!")

"""
Python utilizes a system, which is known as “Call by Object Reference” or “Call by assignment”.

"Call by assignment": is a way to do pass by value
For mutable simple objects (eg int/float/tuples) calls are
by value, ie., at the time of call these values get assigned
to args.
For immutable objects such as string etc.. calls are
by reference. 
For mutable compound objects(eg, list/set/dict etc) calls 
are by reference

Python variable arguments to function
*kwargs  [star is unpacking operator]
*args:


The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
eg:
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
        
B.
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).
eg:
def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')     


"""
"""
Modules, in general, are simply Python files with a .py extension and can have a set of functions, classes or variables defined and implemented. They can be imported and initialized once using the import statement. If partial functionality is needed, import the requisite classes or functions using from foo import bar.
Futher Explanation:
Modules
Module is an additional built-in type supported by the Python Interpreter. It supports one special operation, i.e., attribute access: mymod.myobj, where mymod is a module and myobj references a name defined in m's symbol table. The module's symbol table resides in a very special attribute of the module __dict__, but direct assignment to this module is neither possible nor recommended.



Packages allow for hierarchial structuring of the module namespace using dot notation. As, modules help avoid clashes between global variable names, in a similary manner, packages help avoid clashes between module names.
Creating a package is easy since it makes use of the system's inherent file structure. So just stuff the modules into a folder and there you have it, the folder name as the package name. Importing a module or its contents from this package requires the package name as prefix to the module name joined by a dot.


Deep Copy:
from copy import copy, deepcopy


Python comprehensions, like decorators, are syntactic sugar constructs that help build altered and filtered lists, dictionaries or sets from a given list, dictionary or set. Using comprehensions, saves a lot of time and code that might be considerably more verbose (containing more lines of code). 


Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself. They are represented by the @decorator_name in Python and are called in bottom-up fashion. [A wrapper on top of actual function]
eg:
@splitter_decorator	# this is executed next
@lowercase_decorator # this is executed first(bottom-up)
def hello():
    return 'Hello World'

hello() 


""""""""""""
What are global, protected and private attributes in Python
Private attributes are attributes with double underscore prefixed to their identifier eg. __ansh.
avoid use protected..
gloabl is available anywhere
"""