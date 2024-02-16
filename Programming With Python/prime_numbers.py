#B.Tech Computer Science And Technology
#202103103510429
#Purv Devenbhai Joshi

from time import time
time_exucution= time()

def primeNator(num):
    for i in range(num+1):
        if i>1:
            for x in range(2,i):
                if i%x == 0:
                    break
            else:
                print(i)
    t_time= time() - time_exucution
    print("The code exucution time is :",t_time)
primeNator(100000)

