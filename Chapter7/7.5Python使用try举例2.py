try:
	print('try...')
	s=int(input('Please input number:'))
	print('Result:',10/s)
except Exception as e:
	print('Exception is:', e)
else:
	print('No error!')
finally:
	print('END')
