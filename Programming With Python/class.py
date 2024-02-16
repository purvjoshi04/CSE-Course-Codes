class student:

    behaviour = "good student"
    branch="CSE"
    def __init__(self,name,age,branch,pythonprogramming):

        self.name=name
        self.age=age
        self.branch=branch
        self.python=pythonprogramming
    def my_Method(self):

        print("you made an explicit call")

std_1=student("Purv",18,"CSE","laguage")
std_2=student("Joshi",19,"CSE","laguage")
    
print(std_1.name,"is", std_1.behaviour,"with age:",std_1.age,"in branch",std_1.branch,"with bad skills in programming",std_1.python)
print(std_2.name,"is", std_2.behaviour,"with age:",std_2.age ,"in branch ",std_1.branch)
    

   