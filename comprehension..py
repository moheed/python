print("Hello World!")
"""
Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true. Provide an implementation for filter using list comprehensions.
"""

def myfilter(func, alist:List) ->List:
    return [x for x in alist if func(x)]

def even(x): return x%2==0

f=filter(even, range(10))
for x in f:
    print(x)
mf=myfilter(even, range(10))
for x in mf:
    print(x)
    
#multiple for in list comprehension    
blist=[(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0]
#print(blist)

"""
Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.
"""
def triplets(n: int)->List:
    
    #generate all (x,y) pair x,y<=n
    #check and filter what all result in z<=n
    #return the list
    result=[(x,y, (x+y)) for x in range(n) for y in range(x,n) if (x+y)<=n]
    return result
#print(triplets(4))

"""
Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
"""
def array(row: int, col: int) -> List:
    n=[[None]*col]*row
    print(n)
array(3,4)