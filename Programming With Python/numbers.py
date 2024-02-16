with open("numbers.txt",'r')as f:
    a=f.readlines()
    no_a=[]
    for element in a:
        no_a.append(int(element.strip()))

def fun(b):
    maximum=a[1]
    minimum=a[0]

    for i in range(len(a)):
        if a[i]>maximum:
            maximum=a[i]
        elif a[i]<minimum:
            minimum=a[i]
    return(maximum,minimum)

z=fun(a)
print(z)
