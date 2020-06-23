import concurrent.futures
import time
def do_sth_else():
	print("did sth else")
	
def do_something(sleeptime=1):
	if sleeptime !=None:
		print("sleeping for", sleeptime)
	else:
		print("sleeping default time:", sleeptime)
	time.sleep(sleeptime)
	print("done sleeping")
	return sleeptime
with concurrent.futures.ThreadPoolExecutor() as tpe:
	#f1=tpe.submit(do_something, 1)#add do_something to pool for future execution.
	#f2=tpe.submit(do_something, 2)#add do_something to pool for future execution.
	
	my_threads=[tpe.submit(do_something,i) for i in range(10)]
	for t in concurrent.futures.as_completed(my_threads):
		print (t.result())
		