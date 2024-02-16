class C:
    def __init__(self,c_learning,name_professor):
      self.c_learning=c_learning
      self.name_professor=name_professor

    def display(self):
        print("Your C language learning skills is ",self.c_learning)
        print("your c language professor is ",self.name_professor)

class Python:
    def __init(self,py_learning,name_professor):
        self.py_learning=py_learning
        self.name_professor=name_professor

    def display(self):
         print("Your python language learning skills is ",self.py_learning)
         print("your python language professor is ",self.name_professor)

class Web_Designing:
    def __init__(self,wd_learning,name_professor):
         self.wd_learning=wd_learning
         self.name_professor=name_professor

         print("Your web designing language learning skills is ",self.wd_learning)
         print("your web designing language professor is ",self.name_professor)

class student(C,Python,Web_Designing):
    def __init__(self,std_collage,std_name,std_enroll_no,std_course):
        self.std_collage="Uka Tarsadia University"
        self.std_name=std_name
        self.std_enroll_no=std_enroll_no
        self.std_course=std_course
    def display(self):
       print("Collage  Name is :",self.std_collage)
       print("Student Name is :",self.std_name)
       print("Enroll Number Name is :",self.std_enroll_no)
       print("Course Name is :",self.std_course)

obj=student(input(),input(),int(input()),input())
obj.display()

obj_c=C()
obj_c.display

obj_py=Python()
obj_py.display()

obj_wd=Web_Designing()
obj_wd.display()



