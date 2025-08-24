#wraping the data and method in a single unit is called encapsulation
#encapsulation is a pillar of oop using this concet we can hide the internal infomartion from unauthorized user example (ATM, BIKE EXCELETOR)
'''class EcExample:
  def __init__(self):
    self._name="Shilpa Singha" #public: we can acces outside of the class
    self._id=125  #private: we can access only within class
    self._marks=84
obj=EcExample()
print(obj._name)
print(obj._id)
print(obj._marks)''' 


'''class EcExample:
  def __init__(self):
    self._name="Shilpa Singha" #public: we can acces outside of the class
    self._id=125  #private: we can access only within class
    self._marks=84
  def display(self):
    print(f"My name is={self._name},ID={self._id} and MARKS={self._marks}")
obj=EcExample()
obj.display()'''


'''class Car:
  def my_method(self):
    print("I am car class")
#how to create object
obj=Car()
obj1=Car()
obj.my_method()
obj1.my_method() '''
'''class Car:
  print("I am car class")
obj=Car() '''

# class Car:
#   def __int__(self,name,price):
#     self.name=name
#     self.price=price
#     price(f"Name={self.name} Price={self.price}")
# car1=Car('Volvo',785555)
 
'''class Car:
  def __init__(self):
    print("I am Non Perametarize Constractor")
car1=Car() '''

#Inheritance
'''class Car:
  def display1(self):
    print("I am car class")
class volvo(Car):
  def display2(self):
    print("I am volvo class")
v1=volvo()
v1.display1()
v1.display2()'''

'''class Car:
  def display1(self):
    print("I am car class")
class volvo(Car):
  def display2(self):
    print("I am volvo class")
class Mahindra(volvo):
  def display3(self):
    print("I am Mahindra class")
v1=Mahindra()
v1.display1()
v1.display2()
v1.display3()'''


'''class P1:
    def display1(self):
        print("I am parent1 class")
class P2:
    def display2(self):
        print("I am parent2 class")
class P3:
    def display3(self):
        print("I am parent3 class")
class C1(P1,P2,P3):
    def display(self):
        print("I am chid class")
obj=C1()
obj.display()
obj.display1()
obj.display2()
obj.display3()'''

'''class Base:
    def display1(self):
        print("I am Base class")
class d1(Base):
    def display2(self):
      print("I am derived1 class")
class d2(Base):
    def display3(self):
      print("I am derived2 class")
class d3(Base):
    def display4(self):
      print("I am derived3 class")
obj=d3()
obj.display1()
obj.display4()'''


#method overriding
'''class Car:
  def display(self):
    print("I am car class")
class Volvo(Car):
  def display(self):
    print("I am volvo class")
    super().display()
obj=Volvo()
obj.display()'''

#method overloading
# class Sum:
#   def add(a,b):
#     print(a+b)
#   def add(a,b,c):
#     print(a+b+c)
#   def add(a,b,c,d):
#     print(a+b+c+d)
# obj=Sum()
# obj.add(10,20,30,30)
# obj.add(10,20,30)
# obj.add(10,20)

#abstract class
from abc import ABC,abstractmethod
class Employee(ABC):
  @abstractmethod
  def salary(self):
    pass
class Manager(Employee):
  def salary(self):
    print("Manager salary =",98000)
obj=Manager()
obj.salary()

    