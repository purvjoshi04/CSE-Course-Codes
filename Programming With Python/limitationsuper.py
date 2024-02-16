


class university:
    def __init__(self,department,name) :
        self.department=department
        self.name=name
    def dipplay(self):
        print("your name is :",self.name)
        print("you are from",self.department,"deparment")
        print("student name is",self.name,"and he is belong to the ",self.department)

class info(university):
    
  def __init__(self):
   print(self.department,"is belong to UTU")

class location(university):
    def __init__(self):
        university. __init__(self,"CSE","Purv")
        university.dipplay(self)

obj=location()