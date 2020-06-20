print("Hello World!")
#natural numbe
#fibonacii
#square.
import math as m
def findcase(arr:List[int]) -> str:
    #check if natural numbers
    prev=arr[-1]
    count=0
    if len(arr)<=2:
        return "Cant decide/inval ip"
    count=0
    for x in reversed(arr):
        if prev-x ==1:
            count+=1
        prev=x
    if count==3:
        return "Natural"
    
    first=m.isqrt(arr[0])
    count=0
    for i,x in enumerate(arr):
        #print(first+i)
        if (first+i)*(first+i) ==x :
            count+=1
    
    if count==3:
        return "Square"
    if arr[-1]==arr[-2]+arr[-3] :
        return "Fib"
    
    return "None"

print(findcase ([9,16,25]))

print(findcase([5,6,7,8]))
print(findcase([3,7,9]))
print(findcase([3,5,8]))

        
        
    
    