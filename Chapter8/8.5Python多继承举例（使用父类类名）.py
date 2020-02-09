class Base:
    def __init__(self):
        print('This is Base init function')
#A单继承自Base类
class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('This is init function of A')
#B单继承自Base类
class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('This is init function of B')
#C多继承自A类和B类
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('This is init function of C')
#实例化一个C类的对象c
c = C()
