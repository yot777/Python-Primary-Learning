class Student():
    name =''
    age =0
    grade =''
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.grade = g
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
class Speaker():
    topic =''
    name =''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我演讲的主题是 %s"%(self.name,self.topic))
#多重继承
class Sample(Student,Speaker):
    def __init__(self,n,a,g,t):
        Student.__init__(self,n,a,g)
        Speaker.__init__(self,n,t)

person = Sample("Tim",10,4,"Python")
#方法名相同，默认调用的是在括号中排前的父类的方法
person.speak()
