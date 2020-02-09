class Person():
	#类属性
	num=0
	def __init__(self,name):
		self.name=name  #实例属性
		n=0
		n+=1               #实例属性每次调用会从初始的值开始
		Person.num+=1      #类属性每次调用会保留上次调用的值，类属性的调用要加类名
		print("name=",name)
		print("n=",n)
		print("Person.num=",Person.num) 

a=Person("小明")
b=Person("小陈")
c=Person("小李")   