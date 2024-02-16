my_list=[]

a=int(input("enter number :"))

for i in range(a):
    c=int(input("enter number :"))
    my_list.append(c)
print(my_list)

def sub():
    sub=my_list[0]
    for i in range(1,a):
        sub-=my_list[i]
    return sub
b=sub()
print(b)

    