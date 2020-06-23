

def trace_calls(func):
	'a trace decorator that logs function arguments and results during execution time:'
	def wrapper(*args, **kwargs):
		print("Calling function:", func.__name__, "args:", *args, "kwargs:", **kwargs)
		func(*args, **kwargs)
	return wrapper
@trace_calls
def f1(n:int) -> int:
	if n>0:
		print("times called:", n)
		f1(n-1)
	else:
		pass
#Note none of this needed for a single script
#only if there are multiple files, and you want to enforce
#package execution from certain file, you do following.
def main():
    f1(5)
if __name__=="__main__":
    main()