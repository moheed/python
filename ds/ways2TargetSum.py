print("Hello World!")

def ways_to_sum(arr:List[int], t:int) -> int:
    #Find number of ways to get the sum t from elements of arr
    amap=dict()
    count=0
    for i,x in enumerate(arr):
        diff=t-x
        if diff in amap:
            count+=1
        amap[x]=i
    print(count)
    return count

a=[1,3,7,9,10,11]
t=12
ways_to_sum(a,t)