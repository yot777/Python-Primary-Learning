def func1():
	s=int(input('Please input number:'))
	if s==0:
		raise Exception('除数不能为0！')
	print('Result:',10/s)
try:
	func1()
except Exception as err:
	print('错误信息是：',err)
else:
	print('No error!')
