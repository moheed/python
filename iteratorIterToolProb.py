"""
1. Available common functions:
    a. chain – chains multiple iterators together.
    b. izip - iterable version of zip
"""
#Problem 8: Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.
from typing import Tuple
def peep(it)-> Tuple:
    ###Using class to implement iterator wont 
    #help in avoiding removal of first item.
    
    class mit:
        def __init__(self, it):
            self.it=it
        def __iter__(self):
            return self.it
        def __next__(self, item=None):
            if item:
                yield item
                item=None
            yield next(self.it)
        def send(self, item):
            self.__next__(first)
    
    
    myit=mit(it)    
    first=next(it)
    myit.send(first)
    return (first,myit)
it=iter(range(5))
print(it)
x,it1=peep(it)
print(x, list(it1))
    