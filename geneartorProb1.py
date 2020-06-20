#Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
from typing import TypeVar, Iterable, Tuple, Union, List #all these are aliases

"""
NOTE: 
1. file is an iterable object, hence can be used with for-loop or
any other function that accepts iterator.
eg. list(f) or f.readlines() will give you list of all lines in file
readline() returns single line
f.read() returns entire file as string
opening/closing: better use with: 'with file_method as fd', gaurantee close
even on exception
"""
Response=Union[str,None]
#a generator which returns line >40
def printline_40plus(filenames:List[str]) -> Response:
    for fname in filenames:
        with open(fname, "r") as file:
            #data=file.read()
            line=file.readline()
            if (len(line)>40):
                yield line
#NOTE: generators are iterators and hence sequence.
#def take(howmuch, seq):#take howmuch element from seq
p=printline_40plus(["somefile.txt", "b.txt"])
print(p)
next(p)
        
    
