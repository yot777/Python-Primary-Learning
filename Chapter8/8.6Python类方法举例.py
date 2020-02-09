class Animal():
	#类属性
	num=0
	#实例方法
	def __init__(self):       #实例方法的默认参数是self
		#实例属性
		self.name="小花"

	def test1(self):
		print(self.name)

	@classmethod  #类方法
	def test2(cls):           #类方法的默认参数是cls
		cls.num=100
		print(cls.num)

cat=Animal()               #实例animal
cat.test1()                #实例可以调用实例方法test1
#Animal.test1()               #类不能调用实例方法test1
cat.test2()                #实例可以调用类方法test2
Animal.test2()                #类调可以用类方法test2
