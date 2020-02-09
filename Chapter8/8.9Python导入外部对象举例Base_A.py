class Base:
    def __init__(self):
        print('This is Base init function')
#A单继承自Base类
class A(Base):
    def __init__(self):
        Base.__init__(self)
    def printA(self):
        print('This is init function of A')
#实例化A的对象a
a=A()
a.printA()