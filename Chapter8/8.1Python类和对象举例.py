#类名：Dog（类名的第一个字母一般是大写）
class Dog:
  #定义一个构造方法要包含类所拥有的全部属性，构造方法的第一个参数必须是self不能变，接下来是各个属性名
  def __init__(self,types,name,age):
    self.types=types
    self.name=name
    self.age=age
  #方法：intro （方法名的第一个字母一般是小写，只有一个参数self）
  def intro(self):
    print("我是一只%s,名字是%s,年龄是%d岁" %(self.types,self.name,self.age))

#实例化狗狗1，类型是泰迪，名字是小黑，年龄是3岁
dog1=Dog('泰迪','小黑',3)
dog1.intro()
#实例化狗狗2，类型是拉布拉多，名字是旺财，年龄是5岁
dog2=Dog('拉布拉多','旺财',5)
dog2.intro()
