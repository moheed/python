def take_nonmut(astr:str, alist:[int])->str:
	asl=len(astr)
	all=len(alist)
	#astr[al-1]='X' #wrong string object wont support modification
	alist[all-1]='X'
	print(astr)
	print(alist)
	#return astr
	return alist

mystr="Moheed"
mylist=['M','o','h','e','e','d']
print(take_nonmut(mystr, mylist))#returned list is modified.