dog_age = int(input('Age of the dog: '))
human_age=0
if dog_age == 1:  
	print('This dog is about 14 human years old.')
elif dog_age == 2:  
	print('This dog is about 22 human years old.')
elif dog_age > 2:
	human_age = 22 + (dog_age -2)*5
	print('This dog is about '+str(human_age)+' human years old.')
else:
	print('Input Error!') 
