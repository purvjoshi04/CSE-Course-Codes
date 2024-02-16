file_obj = open ("Purv_Joshi",'w')
file_obj.write("Hello,purv joshi from this side.\n")
file_obj.write("Hope you are doing well.\n")
file_obj.close()

with open("Purv_Joshi",'r') as f:
    print(type(f.readline()))
    print(type(f.readlines()))
    print("output\n")
    f.seek(0)
    print(f.readline())
    print(f.tell())
    f.seek(0)
    print(f.readlines())


