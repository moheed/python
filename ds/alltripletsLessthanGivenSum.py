#input [1,2,3,4,5,0]
#target=4

def tripletLessthan(arr:[int], target:int) -> int:
	#print all triplets
	arr.sort()
	for x in arr:
		print("first nest", x)
		for y in arr:
			print("\tsecond nest", x,y)
			if y>x:
				for z in arr:
					print("\t\tthird nest", x,y,z)
					if z>y and x+y+z < target:
						print (x, y,z)
		
	#result=[[x,y,z] for x in arr for y in arr if y>x for z in arr if z>y and x+y+z < target]
	#for x in result:
	#	print(x)
		
#arr=[1,2,3,4,5,0]
arr=[5, 1, 3, 4, 7]  
#1,3,4,5,7
target=12
tripletLessthan(arr,4)
	