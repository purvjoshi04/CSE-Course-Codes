


from msilib.schema import SelfReg


class university:
     
         name=input("Enter name :")
         year_of_estd=int(input("Enter sthapna day:"))
         city=input("Enter your city:")

class professor(university):
    def __intit__(self,lab_assitant,office_assitant,peon):
        self.lab_assitant=input()
        self.office_assitant=input()
        self.peon=input()

class lab_assitant(university):
    designation="Lab_assitant"

    highest_qualification=input("Enter your highest qualification :")
    year_of_joining=int(input("Enter your joining year:"))

    name_of_institute=input()
    def __init__(self):
        print(self.lab_assitant)
        



obj=university()
obj.pro()

obj_lab=lab_assitant()


