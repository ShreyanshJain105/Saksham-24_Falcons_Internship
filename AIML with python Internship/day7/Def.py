'''==========================================================[def function]==============================================='''

 def one():
    print("i am one function")
 
 def fun(one):
    a,b,c,d=11,12 ,13,14
    
    
    print(one)
    one()
    return a,b,c,d
   
    

'''
def fun1():
    print("this is fun1")

def fun2(ref_var):
    print("this is fun2\n")
    ref_var()



fun2(fun1)
'''


'''
def one():
    print("i am one function")
 
def fun(one):
    a,b,c,d=11,12 ,13,14
    
    
    print(one)
    one()
    
    return a,b,c,d
    



fun(one)
'''



def outer():
    def inner():
        a=10

        print("i am inner")
        return a

        return inner

        ans=outer()
        print(ans)
        ans()


'''==========================================================[Arguement]==============================================='''


def fun(a,b,c):  #parameters
    print(a,b,c)

fun(b=10,a=34,c=34 ) #arguement


# default argue

def fun(a,b,c=45):  #parameters
    print(a,b,c)

fun(b=10,a=34)  #arguement

'''==========================================================[Pattern]==============================================='''
def funx(*args):
    print(args)
    print(type(args))

    for i in args:
        print(i,end="")



funx(1,2,3,4)
funx(1,2,3,4,5)

'''==========================================================[Keyword Arguement ]==============================================='''
keyword arguement 
def aa(**args):
    # print(args)
    # print(type(args))

    for i,j in aa.items():
        print("key: " ,i, " " ,"value ", j)

aa(name="student" , classs="python" , age="50" , work="software ")    



'''==========================================================[Global function]==============================================='''


a=21

def fun():
    
    global a
    a=455804

    print(a)


fun()
print(a)


'''==========================================================[Nonlocal function]==============================================='''


a=10
def fun():
    b=40
    def inner():

        nonlocal b
        b=98
        print(b)

        inner()
        print(b)

fun()        