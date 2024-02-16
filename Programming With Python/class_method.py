"""from re import X

from unicodedata import name


class student:
    name="purv"

    def display(self):
        self.name()
        x= print("self.name")

class person(student):
   

p=student()
p.get(name)
p.display()



class student():
    def person(name):
        name="purv"

class person(student):
    print()

class Person:
  def get(self, fname):
    self.firstname = fname
    

  def printname(self):
    print(self.firstname)

class Student(Person):
  def get(self, fname):
    Person.get(self, fname)

x = Student()

print()"""
#Multiple class
class base:
  name="Purv"
  def display(self):
    print("hello",self.name)

class derived(base):
  surname="Joshi"
  def display(self):
    print("hii!!",self.surname)


class superDerived(derived):
  def display(self):
    print("Nice to having you",self.name,self.surname)


base_obj=base()
base_obj.display()

deri_obj=derived()
deri_obj.display()

super_obj=superDerived()
super_obj.display()
x=issubclass(derived,base)
y=issubclass(superDerived,derived)
print(x)
print(y)


