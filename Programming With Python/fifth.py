from ast import Return


my_list=[]
x=int(input("Enter total number :"))

for i in range(x):

    a=int(input("Enter numbers :"))

    my_list.append(a)

print(my_list)

"""def add():

 add=0

for i in range(len(my_list)):
   #add+=my_list[i]

type(add)"""

def add():
    add=0
    for i in range(len(my_list)):
        add+=my_list[i]
    return add
b=add()
print(b)
     



