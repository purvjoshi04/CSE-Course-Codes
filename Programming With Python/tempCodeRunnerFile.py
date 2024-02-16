"""class democlass:
    def  fun(self):
        print("hello ")

purv=democlass()
purv.fun()

class vehicle:
    def get(self,type,color):
        self.color=color
        self.type=type

    def put(self):
        print(self.color)
        print(self.type)

v_obj=vehicle()
v_obj.get("car","red")
v_obj.put()



class sample:
    x=2 #class variable
    def get(self,y): #y is instance variable
        self.y=y
s1=sample()#instances

s1.get(3)#access attributes
print(s1.x,s1.y)

s2=sample()#instances
s2.y=4
print(s2.x,s2.y)"""


class stdmark:
   # __stdmarks=15
    __x=int(input("enter a number:"))
    def display(self):
        print("marks=",self.__x)

std_obj=stdmark()
std_obj.display()
print("marks=",std_obj.__x)
