from multiprocessing.sharedctypes import Value


my_list=[]
x=int(input("Enter total number :"))

for i in range(x):

    a=int(input("Enter numbers :"))

    my_list.append(a)

"""print(my_list)
print(max(my_list))
print(min(my_list))

def max_val(a):
  Value= a[0] 
  for value in a(x): 
    if value > max_val: 
      max_val = value
  return max_val

print("The maximum value is:",max_val(my_list))

def max_val():
    
    

    for i in range(len(my_list)):
        max_val>=my_list[i]
    return max_val
b=max_val()
print(b)"""

def fun(b):
  maximum=my_list[0]
  minimum=my_list[0]

  for i in range(1,x):

    if my_list[i]>maximum:
      maximum=my_list[i]

    elif my_list[i]<minimum:
      minimum=my_list[i]
      
  return (maximum,minimum)

z=fun(my_list)
print(z)

