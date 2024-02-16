
from unicodedata import name


class staff:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class teacher(staff):
    def __init__(self,department, salary):
        self.department=department
        self.salary=salary
        super().__init__("Purv","28")

    def display(self):
        print(self.name)
        print(self.age)
        print(self.department)
        print(self.salary)
obj=teacher(102039,"B.tech CSE")
obj.display()
x= issubclass(teacher,staff)

print(x)


        