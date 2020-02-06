def func(n):
	for i in range(2,n):
		print("i=",i)
		print("i*i=",i*i)
		yield i*i*i

for s in func(5):
	print("s=",s)
