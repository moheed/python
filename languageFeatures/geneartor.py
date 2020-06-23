print("Hello World!")
"""
Revision Notes:

1. A generator is a function that produces a sequence of results instead of a single value.
2. Generators simplifies creation of iterators. 
3. uses yield
   yield statement is executed the function generates a new value.
4. A generator is an iterator [No need to worry about iterator protocol]
5. use the word “generator” to mean the genearted object and “generator function” to mean the function that generates it.
6. How it works?
   a. When a generator function is called, it returns a generator object without even beginning execution of the function.
   b. on a next() method call on generator object, gfun starts executing. and
   stops as soon as it yield a value and returns this value to next()
   c. on second call it resumes execution.. yeilding more values if any
   d. otherwise raising exception StopIteration
7. These generator functions can run infinitely

8. Generator Expressions are generator version of list comprehensions.
    8.a They look like list comprehensions, but returns a generator back instead 
    of a list.
>>>a = (x*x for x in range(10))
>>> a
<generator object <genexpr> at 0x401f08>
>>> sum(a)
285
9. generator expressions can be used as arguments to various functions that consume iterators.
eg. 
>>> sum(x*x for x in range(10))
285
Question: Find  first 10 pythogorain triplets.(x,y,z): z**2=x*82+y**2
>>> pyt = ((x, y, z) for z in integers() for y in range(1, z) for x in range(1, y) if x*x + y*y == z*z)
>>> take(10, pyt)