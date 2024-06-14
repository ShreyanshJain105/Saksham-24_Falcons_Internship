# numpy
import numpy as np 
nn = np.array([1,2],[4,3])
print(nn)
print(type(nn))
print(nn)


import numpy as np
ans=np.full((5,5),10)
print(ans)

print(np.arrange(10,100,35))

print(np.random.randint(10,200,23))
arr= np.array1([1,2],[2,3],[2,3],[2,3])
print(np.shape(arr))
arr.shape=(2,4)
print(np.shape(arr))
print(arr)

import numpy as np
n=np.array(
    [
    [1,2,3,4],
    [4,3,2,1]

    ]  )
print(n)
print(type(n))

import numpy as np
ans=np.full(  (3,5)  , 11)
#print(ans)


#arange()
#print(np.arange(10,50,5))

# random
#print(np.random.randint(10,100,5))
# arr=np.array( [
# [1,2],
# [2,3],
# [3,4],
# [4,5]
#                ] )
# #print(np.shape(arr))
# arr.shape=(2,4)
# print(np.shape(arr))
# print(arr)

import numpy as np

n1=np.array([1,2,3,4 ,5,6])
n2=np.array([5,6,7,8])




print(np.vstack((n1,n2)))
print(np.hstack((n1,n2)))
print(np.column_stack((n1,n2)))


intersection and difference

ans=np.intersect1d(n1,n2)
print(ans)
print(np.setdiff1d(n1,n2) )
print(np.setdiff1d(n2,n1))



np.sum((n1,n2))
ans=np.sum([n1,n2],axis=0)
ans1=np.sum([n1,n2],axis=1)
print(ans)
print(ans1)

import numpy as np
n=np.array([1,2,3,4,7,2,1])

mathamatics
print(n+2)
print(n-2)
print(n*2)
print(n/2)


#mean ,median ,standard deviation
print(np.mean(n))
print(np.median(n))
print(np.std(n))


import numpy as np
#matrix

m=np.array(  [
              [1,2,3]
              ,[4,5,6],
               [7,8,9]

              ]  )


  #  1  4  7
  #  2  5  8
  #  3  6   9
n=np.array([[1,1,1]
          ,[2,2,2],
  [3,3,3]])

#print(m,"\n")
#print(m[1])
#print(m[ : ,  2])

#print(m[1:3 ,0: 2])


#transpose
# print("\n")
#print(np.transpose(m))


# dot multipiccation
#print(m.dot(n))
# print("\n")
#print(n.dot(m))



# save and load numpy array

import numpy as np
n=np.array([10,20,30,40])


np.save("numpy_array",n)

np.load("numpy_array.npy")