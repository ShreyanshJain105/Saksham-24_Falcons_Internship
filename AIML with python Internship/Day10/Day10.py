# import Module
# var=10

# def task():
#     print("this isfunction ")
#     print(var)

# task()    

# ans=Module.calculator(100,200)
# print(ans)

'''==========================================================[Math]==============================================='''


'''
import math

print(math.pow(2,3))

# a=math.pow(2,3,5)
# print(a)

'''==========================================================[log operation ]]==============================================='''
 

print(math.log(10))

print(math.ceil(6.87))  #upper value 
print(math.floor(6.86))  #bottom value 

print(math.fabs(-124.5))   # thhis will convert negative to positive 


print(math.sin(45))   # sin tan cos

print(math.tan(90))

'''

# import random
'''
from random import*
print(random())

print(randrange(5,10))

print(randint(10,20))

s='i am string '

# choice(s)
print(choice(s))   # random value in string 

l=[1,2,3,4,5,67,'namde']

print(choice(l))  # randomvalue in list

t=(19,2,398)
print(choice(t))   # ranndom value in tuples

print(shuffle(l))   # suffle the values in list 
print(l)

'''


import statistics as s
# from  statistics as import*

l=[1,2,3,4,5,4,5]
print(s.mean(l))

print(s.median(l))

print(s.mode(l))

print(s.mode(l))

t=[1,2,3,4,5,4,5,5,5,4]
print(s.mode(t))



'''==========================================================[Doc string ]==============================================='''

'''Doc string in python '''
# doc string => understand to wahat code we write 

def func():

    '''this is function about the printig the value 
    '''

print("hiii")

func()


