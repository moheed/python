import base_modules
import concurrent.futures


with concurrent.futures.ThreadPoolExecutor() as tpe:
	my_threads=[tpe.submit(do_something,i) for i in range(10)]
	for t in concurrent.futures.as_completed(my_threads):
		print (t.result())
		
		
