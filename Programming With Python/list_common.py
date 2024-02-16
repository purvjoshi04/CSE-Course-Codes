"""def number_list_creator():
 with open("list.txt",'r') as file:
       list=file.readlines()  
number_list=[]

for element in list:
    number_list.append(int(element.strip()))  
print(number_list)"""

txt_file=open("list.txt",'rt')
data=txt_file.read()
x=str(input("Enter the number that you want to search:"))

occurance=data.count(x)
print(data,"The occurance of number in list.txt is :",occurance)

