class Animal:
	def __init__(self,types,name,age):
		self.types=types
		self.name=name
		self.age=age
	def intro(self):
		print('我是一只%s,名字是%s,年龄是%d岁' %(self.types,self.name,self.age))
	def run(self):
		print('我飞快的跑')


class Dog(Animal):
	def __init__(self,types,name,age,hair):
		'''初始化父类的属性，再初始化狗这个子类的特有属性'''
		super().__init__(types,name,age)
		self.hair=hair
	def intro(self):
		print('我是一只%s,名字是%s,年龄是%d岁,毛发颜色是%s' %(self.types,self.name,self.age,self.hair))
	def look(self):
		print('我会看家门')

class Cat(Animal):
	def __init__(self,types,name,age,ear):
		'''初始化父类的属性，再初始化猫这个子类的特有属性'''
		super().__init__(types,name,age)
		self.ear=ear
	def intro(self):
		print('我是一只%s,名字是%s,年龄是%d岁,耳朵长度是%s' %(self.types,self.name,self.age,self.ear))
	def catches(self):
		print('我会抓老鼠')

dog1=Dog('泰迪','小黑',3,'棕色')
dog1.intro()
dog1.run()
dog1.look()

dog2=Dog('拉布拉多','旺财',5,'金黄色')
dog2.intro()
dog2.run()
dog2.look()

cat1=Cat('波斯猫','小咪',2,'短耳')
cat1.intro()
cat1.run()
cat1.catches()

cat2=Cat('暹罗猫','花花',4,'长耳')
cat2.intro()
cat2.run()
cat2.catches()