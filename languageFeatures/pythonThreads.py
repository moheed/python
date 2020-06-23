import threading as thread

def do_sth_else():
	print("did sth else")
	
def do_something(sleeptime=1):
	if sleeptime !=None:
		print("sleeping for", sleeptime)
	else:
		print("sleeping default time:", sleeptime)
t1=thread.Thread(target=do_something)
t2=thread.Thread(target=do_sth_else)
t1.start()
t2.start()
#ensure t1 and t2 dont finish before the parent.
t1.join()
t2.join()
threadlist=[]
for _ in range(10):
	t=thread.Thread(target=do_something)
	t.start()
	threadlist.append(t)
for t in threadlist:
	t.join()


for i in range(10):
	t=thread.Thread(target=do_something, args=[i])
	t.start()
	threadlist.append(t)
for t in threadlist:
	t.join()
	