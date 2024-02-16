#creating two base class and only with one inheritence

#base class 1
class base1:
    
    name="Purv"
#base class 2
class base2:
    surname="Joshi"

#derived class
class Inheri(base1,base2):
   def __init__(self):
       print(self.name ,"'s surname is ",self.surname)
       
    
obj=Inheri()

