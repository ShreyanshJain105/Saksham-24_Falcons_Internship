
l=[10,9,-10,89,23]

l.sort()
print(l)


l.sort(reverse=True)                   #It effect on original list
print(l)    

ans=sorted(l)                          #It does not effect on original list
x=sorted(l,reverse=True)
print(ans)
print(l)

print(x)
print(l)

l1=[1,2,3,'name']
l2=[10,20,30]

anss=l1+l2

print(anss)

nn=l1*3
print(nn)




# Tupls 
t=(1,2,3,4,5,'string')
print(t)
print(type(t))


# for multiple value assigining

a,b,c=10,20,30.5
print(a)
print(b)
print(c)

aa=1,2,3,4   
print(aa)
print(type(aa))


tt=(1,2,3)
print(tt)


print(len(tt))


(aa,bb,cc)=tt
print(aa)
print(bb)
print(cc)


Y=10
Yb='i am sring'
YY=20

O=(Y,Yb,YY)
print(O)




# slicing in tuples

q=(5,6,7,8,9)
# qq=q[0:-2]
# qq=q[-1:-20:1]    #empty tuples
print(q)

print(len(q))

print(q.count(8))

print(q.index(8))



# isme sort funion appl nahi hoga


# islie use karenge sorted 
w=(100,5,6,-20,7,50,8,9,8)
aaa=sorted(w)
print(aaa)

print(sorted(aaa,reverse=True))  #decending order 

# del It delete whole tuple 
print(w)

print(min(w))
print(max(w))

e=w*3
print(e)

# two tuples adding 

w1=(100,5,6,-20,7,50,8,9,8)
w2=('10','20','30')
w2=w1+w2
ww=w2+w1
print(ww)
print(w1+w2)
print(w2)

