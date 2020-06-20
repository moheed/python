print("Hello World!")
#Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction.
class reverse_iter:
    """
    Revision Note:
    Def1: Iterables can be looped over, and anything that can be looped over is an iterable.
    Def2: Sequences are iterables that have a specific set of features. They can be indexed (from 0 onwards to len-1) 
    Note1: not all iterables are sequences: Eg
        sets, dict, files and generators are not sequence
        hence these can't be indexed.
    Note2: Each iterable have built-in iter() function
        Always returns an iterator.
        Eg:
        >>> numbers = {1, 2, 3, 5, 7}
        >>> coordinates = (4, 5, 7)
        >>> words = "hello there"
        >>> iter(numbers)
        <set_iterator object at 0x7f2b9271c860>
        >>> iter(coordinates)
        <tuple_iterator object at 0x7f2b9271ce80>
        >>> iter(words)
        <str_iterator object at 0x7f2b9271c860>
    Note3: once we have iterator, use next(it) to get next
            item.
    Note4: Iterators are stateful, consumed item wont be        there.
    Note5: The iterator protocol is a fancy way of saying
    "how looping over iterables works in Python." ie. 
    next()/iter() 
    
    Note6: iterator protocol is used by:
        a.for loops
        b. multiple assignment
        c. star expression eg:
            print(*numbers)#prints all numbers
        d. and many built-in rely on it-proto
            eg. unique_num=set(numbers)
    Note7: Iterators are Iterables.[you can get an iterator
    from an iterator using the built-in iter function:]
    iter called on iterator gives itself back.
    SUMMARY:Iterators are iterables and all iterators 
        are their own iterators.
    NOTE7.1: To check if an iterable is iterator:
        def is_iterator(iterable):
            return iter(iterable) is iterable#same object
    BIGSUMMARY:
    a.An iterable is something you're able to iterate over
    b. An iterator is the agent that actually does the 
        iterating over an iterable
    c. Additionally, in Python iterators are also iterables
        and they act as their own iterators.So iterators
        are iterables
        c1. iterators have no lenght/no index: so only
            use with next()
    Note8: A generator is an iterator
    1. built-in next() and iter() methods calls object's(iterator's) __next__() and __iter__()
    2. Many built-in methods that consume iterable objects:
    join()
    list()
    str()
    2.1 Many built-in functions accept iterators as arguments.
    eg.[come here back after you understand Iteration Protocol to be more clear.]
    list(iterator)
    str(iterator)[str does not consume Iterator, but iterables]
    sum(iterator)
    Note: In the above case, both the iterable and iterator are the same object.
    Note2: If both iteratable and iterator are the same object, it is consumed 
        in a single iteration
    3. Any object that can be for looped is iterable.
    4. iterable-objects are consumed, by calling iter() on the object which returns
    associated iterator.(internally it calls __iter__()
    __iter__() method(on object) returns iterator which then is consumed by 
    __next__(), untill StopIteration is raised.
    5. Iterators are implemented as classes.
        a.An iterator must have __init__(), __iter__(), __next__()
        b. Must raise StopIteration when no more items
    """
    ##Problem 1: Write an iterator class reverse_iter, 
    ##that takes a list and iterates it from the reverse direction.
    #4 things, __init__,__next__,__iter__ and raise StopIteration
    def __init__(self, alist:List) :# gives error-> reverse_iter:
        
        self.alist=alist
        self.i=len(alist)-1
    def __iter__(self):# -> reverse_iter:
        return self
    def __next__(self) : #cant mention return type here.. as list could be anything
        if self.i<0:
            raise StopIteration
        v=self.alist[self.i]
        self.i-=1
        return v
it = reverse_iter([1, 2, 3, 4])
print(it)
astr=sum(it)
print(astr)

"""
A. Iterator Protocol in full:
Iterables can be passed to the iter function to get an iterator for them.

Iterators:

Can be passed to the next function, which will give their next item or raise a StopIteration exception if there are no more items
Can be passed to the iter function and will return themselves back

The inverse of these statements also holds true:

Anything that can be passed to iter without a TypeError is an iterable
Anything that can be passed to next without a TypeError is an iterator
Anything that returns itself when passed to iter is an iterator
That's the iterator protocol in Python.

B. Iterators enable laziness
Iterators allow us to both work with and create lazy iterables that don't do any work until we ask them for their next item.
Because we can create lazy iterables, we can make infinitely long iterables. And we can create iterables that are conservative with system resources, can save us memory, and can save us CPU time.
BUILT in iterator example:
enumerate()
reversed()
zip()
map()
filter()
file-object
C. Usually when we want to make a custom iterator, we make a generator function: instead of writing iterator class.
generator function/generator-expression is equivalent to the class 
And you dont need to care about itProtocol
C.1: generator-fun vs generator-exp:
generator-fun have yield statement
C.2: generator-exp are of type (expr), where expr contains
some looping mechanism to generate results. [like list 
comprehension]
c.3:
Unpacking a dictionary is really the same as looping over the dictionary. Both use the iterator protocol

C4:
When someone says the word "iterable," you can only assume they mean "something that you can iterate over." Don't assume iterables can be looped over twice, asked for their length, or indexed.

Iterators are the most rudimentary form of iterables in Python.
"""