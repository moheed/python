print("Hello World!")
#Write a function my_enumerate that works like enumerate.
def my_enumerate(item):
    #Note: generators dont need to raise StopIteration
    #they dont need to write __next__() and __iter__()
    #methods
    it=iter(item)
    i=0
    while True:
        try:
            yield (i,next(it))
            i+=1
        except StopIteration:
            break
        
x=[1,2,3,4,5]
for i,item in my_enumerate(x):
    print(i, item)
        