class Dog:
  #公有属性
  types = '泰迪'
  name = '小黑'
  age = 3
  #私有属性
  __hair = '棕色'
  def set_hair(self):
    self.__hair='棕色' 
  def get_hair(self):
    return self.__hair

dog1=Dog()
print(dog1.types)
print(dog1.name)
print(dog1.get_hair())