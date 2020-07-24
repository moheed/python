#NOTE: creating list with comprehension creates many
#pecularities.. as python treats list with shallow copy...
#for example

arr=[0]*5  #=== with this method, python only creates one integer object with value 5 and
			#all indices point to same object. since all are zero initially it doesn't matter.
arr[0]=5	#when we modify arr[0], it creates a new int object with val=5 and makes the zero-index point
			#new object.
print(arr)  #this works expected.

#however,
arr2=[[0]*5]*5 #expecting 5x5 matrix filled with zero
print(arr2)
arr2[0][0]=1  #expecting only 0,0 to be 1.. but o/p?
print(arr2)   #[[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
			#HOW all elements of first column are changed... Weired???
#This is because list works in shallow way... as shown for arr(1-d array)
#however, when we declare a 2-d arr, that means all indices in a given inner [](ie col) point to single integer object 0 
#when we update by arr2[0][0]=x, what we are doing is, updating the first element of inner[](ie col)
#since all row-indices for that col point to same object, it updates all first values of given col.

"""
Similarly, when we create a 2d array as “arr = [[0]*cols]*rows” we are essentially the extending the 
above analogy.
1. Only one integer object is created.
2. A single 1d list is created and all its indices point to the same int object in point 1.
3. Now, arr[0], arr[1], arr[2] …. arr[n-1] all point to the same list object above in point 2.

The above setup can be visualized in the image below.
One way to check this is using the ‘is’ operator which checks if the two operands refer to the same object.

Best Practice:
If you want to play with matrix run the LOOP and ensure all mxn objects are allocated.!
# Using above second method to create a  
# 2D array 
rows, cols = (5, 5) 
arr=[] 
for i in range(cols): 
    col = [] 
    for j in range(rows): 
        col.append(0) 
    arr.append(col) 
print(arr) 
"""