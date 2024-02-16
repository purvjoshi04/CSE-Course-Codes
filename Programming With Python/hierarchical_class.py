
class base:
  name="Purv"
 

class base1(base):
    id=429
    def base(self):
        print(self.name,"'s id is:" ,self.id)
class base2(base):
    department="CSE"
    def display(self):
        print(self.name,"'s department name is:" ,self.department)
class base3(base):
    university="Uka tarsadia "
    def dept(self):
        print(self.name,"'s university name is:",self.university)

obj_1=base1()
obj_1.base()

obj_2=base2()
obj_2.display()

obj_3=base3()
obj_3.dept()