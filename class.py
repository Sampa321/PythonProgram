'''class Student:

    name="sampa" ,
    id=123,
    address="Purba Medinipur"
    print(f"Name={name} id={id} address={address}")
obj1=Student()'''

#CONSTRACTOR OR MAGIC METHOD_INIT_()
'''class Student:
    def __init__(self,name,id,college):
        self.name=name
        self.id=id
        self.college=college
    def display(self):
        print(f"{self.name},{self.id},{self.college}")
a=Student("sampa",18,"SVU")
b=Student("sandip",26,"SVU")
c=Student("arpita",18,"SVU")      
#how to called a class method
a.display()
b.display()
c.display() '''

'''class Employee():
    name='Akash',
    id=121,
    company='TCS'
    def employee_information(self):
        print(f"Name={self.name} id={self.id} company={self.company}")
obj=Employee()
# print(obj.name)'''
 
'''class Employee:
  name='Akash' # class variale(name,id,company)
  id=121
  company='TCS'
  def employee_information(self):
    print(f"Name={self.name} id={self.id} comapny={self.company}")
obj=Employee()
obj.employee_information()'''

'''class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def employee_info(self):
        print(f"Name={self.name} Id={self.id} Salary={self.salary}")
obj1=Employee("Prince",121,45000)
obj2=Employee("Antara",567,89000)
obj1.employee_info()
obj2.employee_info()'''

#inheritance:single level inheritance
'''class A:
    def display(self):
        print("I am a Base Class")
class B(A):
    def display1(self):
        print("I am Derived class")
obj=B()
obj.display()
obj.display1()'''

#Multilevel inheritance
'''class Base:
    def display(self):
        print("I am Base Class")
class Derived1(Base):
    def display1(self):
        print("This is derived1")
class Derived2(Derived1):
    def display2(self):
        print("This is derived2")
obj=Base()
obj1=Derived1()
obj2=Derived2()
# print(obj.display())
# print(obj1.display())
print(obj1.display1())
obj2.display() #current object reference
obj2.display1()
obj2.display2()''' 

#multiple inheritance:
'''class Base1:
    def display(self):
        print("This is Base1")
class Base2:
    def display1(self):
        print("This is Base2")
class Derived(Base1,Base2):
    def display2(self):
        print("This is Derived Class")
d=Derived()
d.display()
d.display1()
d.display2() '''

#hierarchical inheritance
'''class Base:
    def display(self):
        print("This is Base Class")
class Child1(Base):
    def display1(self):
        print("This is first child")
class Child2(Base):
    def display2(self):
        print("This is second child")
# ch=Child2()
# ch.display()
# ch.display2()
ch1=Child1()
ch1.display()
ch1.display1()'''

'''class Base:
    def display(self):
        print("I am Base Class")
class Derived(Base):
    def display(self):
        super().display()
        print("Iam derived Class")
obj=Derived()
obj.display()'''
