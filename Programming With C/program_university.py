class university:
    def __init__(self,name,year_of_estd,city):
        self.name=name
        self.year_of_estd=year_of_estd
        self.city=city
    def display(self):
        print("name of university:",self.name)
        print("year of established:",self.year_of_estd)
        print("city:",self.city)
class professor(university):
    def __init__(self,designation,name,highest_qualification,area_of_research,year_of_joining,year_of_experience,name_of_institute):
        self.designation=designation
        self.name=name
        self.highest_qualification=highest_qualification
        self.area_of_research=area_of_research
        self.year_of_joining=year_of_joining
        self. year_of_experience=year_of_experience
        self.name_of_institute=name_of_institute
    def display(self):
        print(self.highest_qualification)
        print(self.area_of_research)
        print(self.year_of_joining)
        print(self.year_of_experience)
        print(self.name_of_institute)

class lab_assistant(university):
    designation="labour"
    def __init__(self,highest_qualification,additional_skills,year_of_joining,name_of_institute):
        self.highest_qualification=highest_qualification
        self.additional_skills=additional_skills
        self.year_of_joining=year_of_joining
        self.name_of_institute=name_of_institute
    def display(self):
        print(self.highest_qualification)
        print(self.additional_skills)
        print(self.year_of_joining)
        print(self.name_of_institute)

class office_assistant(university):
    def __init__(self,highest_qualification,year_of_joining,name_of_institute):
        self.highest_qualification=highest_qualification
        self.year_of_joining=year_of_joining
        self.name_of_institute=name_of_institute
    def display(self):
        print(self.highest_qualification)
        print(self.year_of_joining)
        print(self.name_of_institute)

class peon(university):
    def __init__(self,qualification,year_of_joining,name_of_institute):
        self.qualification=qualification
        self.year_of_joining=year_of_joining
        self.name_of_institute=name_of_institute
    def display(self):
        print(self.qualification)
        print(self.year_of_joining)
        print(self.name_of_institute)
 

obj1=university(input("enter institute name:"),int(input("year of eastablished:")),input("city:"))
obj1.display()
print("enter 1 for professor")
print("enter 2 for lab assistant")
print("enter 3 for office assistant")
print("enter 4 for peon")
class_input=int(input("enter number:"))
if class_input==1:
    obj2=professor(input("designation:"),input("name"),input("highest qualification:"),input("research area:"),int(input("joining year:")),int(input("experience years:")),input("name of institute:"))
    obj2.display()
elif class_input==2:
    obj3=lab_assistant(input("highest qualification:"),input("additional skills:"),int(input("year of joining:")),input("name of institute:"))
    obj3.display()
elif class_input==3:
    obj4=office_assistant(input("highest qualification:"),int(input("year of joining:")),input("name of institute:"))
    obj4.display()
elif class_input==4:
    obj5=peon(input("highest qualification:"),int(input("year of joining:")),input("name of institute:"))
    obj5.display()