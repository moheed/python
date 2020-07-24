#in_list=[11, 22, 5, 15, 25, 3]
#out_list = [[11,22], [5,15,25], [3]]


def list_test(inlist, outlist):
    if not inlist:
        return []
    prev=inlist[0]
    x=[]
    for item in inlist:
        if item >= prev:
            x.append(item)
        else:
            outlist.append(x)
            x=[]
            x.append(item)
        prev=item
    if x:
        outlist.append(x)


in_list=[1,0,1,2,3]
out_list = []
list_test(in_list, out_list)	
print(out_list)
