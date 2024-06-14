# set

a=[]

b=()

c={}
cc={1,2,3,3,2,1,1,1}
print(type(a))
print(type(b))
print(type(c))
print(type(cc))
print(cc)

cc.add(2)
cc.add(34)
cc.add('set')

# cc[0:]   not able to perform indexing 
# print(cc[0])


print(len(cc))
cc.remove(3)

# cc.remove(999)             # when he "999" isnot conain then we have a error
cc.discard('set')
cc.discard(999)              # It does not have an error either it contain or not "999"
print(cc)



s1={1,2,3,3,2,1,1,1,'name',1000}

s2={11,22,33}
# s1.update(s2)
s2.update(s1)

# s1=s1+s2 this is not support set 
print(s1)




ss1={10,20,30,40}
ss2={20,40,50,60}

a22=ss1.union(ss2)
print(a22)

sd=ss1.intersection(ss2)
print(sd)

sdd=ss1.difference(ss2)
print(sdd)

sddd=ss2.difference(ss1)
# sddd=ss2-ss1
print(sddd)

sa=ss1.symmetric_difference(ss2)
print(sa)


# in se pop remove any value 
print(ss1.pop())
print(ss2.pop())

ss11={1,2,3}
ss22={3,2,1}
print(min(ss11))
print(max(ss22))

print(ss11==ss22)
