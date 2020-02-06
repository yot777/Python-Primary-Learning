try:
	print('try...')
	s=int(input('Please input number:'))
	print('Result:',10/s)
except ValueError as e1:
	print('ValueError Exception:', e1)
except ZeroDivisionError as e2:
    print('ZeroDivisionError Exception:', e2)
finally:
	print('END')
