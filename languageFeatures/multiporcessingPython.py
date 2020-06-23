import multiprocessing
def do_sth(i):
	print("sleeping for i")
	time.sleep(i)
	print("slept for:", i, "seconds")
	return i
"""
p1= multiprocessing.Process(target=do_sth)
p2= multiprocessing.Process(target=do_sth)
p1.start()
p2.start()
print(p1.result(), p2.result())
p1.join()
p2.join()
"""
plist=[]

for i in range(10):
	
	p=multiprocessing.Process(target=do_sth, args=[i])
	plist.append(p)
	p.start()
	
for p in plist:
	p.join()

import concurrent.futures

with concurrent.futures.ProcessPoolExecuter() as ppe:
	p1=ppe.submit(do_sth, 1)#add to the process pool
	p1.start()#start the process
	plist = [ppe.submit(<pname> <arg>) for _ in range(10)] #10 proecess in process pool
	#OR
	plist = [ppe.map(do_sth, [arg]) for arg in range(10)]#basically can use map(function, sequence[])run fun 
	#for each item in sequence)
	for p in concurrent.futures.as_completed():#check which one is completed from the plist
		print(p.result())
	
	print("result:", p1.result())
	
if __name__=="__main__":
	multiprocessing.freeze_support()
	main()