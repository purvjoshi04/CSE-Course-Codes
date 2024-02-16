#creating one base class and only with one inheritence

#base class
class base1:
    name="Purv"


#derived class
class Inheri(base1):
   def __init__(self):
       print(self.name)
       
    
obj=Inheri()

       
