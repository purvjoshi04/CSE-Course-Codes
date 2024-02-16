#creating 3 class with 3 diff^ class inheritance

#base class
class base:
  name="Purv"
  def display(self):
    print("hello",self.name)

#inheritance class of base class 
class derived(base):
  surname="Joshi"
  def display(self):
    print("hii!!",self.surname)

#derived class 
class superDerived(derived):
  def display(self):
    print("Nice to having you",self.name,self.surname)


base_obj=base()
base_obj.display()

deri_obj=derived()
deri_obj.display()

super_obj=superDerived()
super_obj.display()
