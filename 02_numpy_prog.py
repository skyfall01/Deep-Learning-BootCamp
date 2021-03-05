import numpy as np #n-multi dimensional list
import os
os.system("cls")  

list1 = [1,2,3]
print(type(list1))
np1 = np.array(list1)

print(np1.ndim)

print(np1[2])
np1[:] #slicing
np1[1:]

list2 = [[[1,2],[3,4]],[[5,6],[7,8]]]
np2 = np.array(list2)
print(np2)
print(np2.ndim)
print(np2.shape)
print(np2[0],"\n",np2[0:2],"dsfdsf",np2[0:2,1,1]) 
os.system("cls")
#np[rows,col,another dimension,......]
#np[:,col] - row matrix(the elements in that col are represented as row matrix)
#np[:,col:col+1] - col matrix (the elements in that col are represented as col matrix)
# np[[row1,row2,....],[col1,col2,....]] - different elemnts present in random rows and col. outputs single row vector with all those elements
#a[2:] = 99 -> broadcasting. replace all elements after 2nd row with 99
list3 = [[1,2,3],[4,5,6],[7,8,9]]
np4 = np.array(list3)
print(np4.ndim)

print(np4[:,1:3])
print(np4[:,1:2])

print(np4[[0,0,1,1,2,2],[1,2,1,2,1,2]])

np4[:,2:] = 90
print(np4)

os.system("cls")


#Functions
'''
arange(start,stop+1,increment/decrement(step size))
'''
np5 = np.arange(80,40,-2) 
print(np5)#80-42 numpy array. 40 wont print since its stop+1(just like slicing)

'''
zeros((row,col),dtype="specify data-type(default=float)") - zero numpy array
ones((row,col),dtype="specify data-type(default=float)") -  ones np arr
'''
np6 = np.zeros(3,dtype=int) #1 row,3 col 
print(np6)
np6 = np.zeros((2,3),dtype=int) #2row, 3 col
print(np6)
np6 = np.ones((3,4))
print(np6)
'''
eye(row,col,dtype="specify data-type(default=float)",k="any number(default=0)(from which diagonal to start)")
'''
np6 = np.eye(3,4)
print(np6)
'''
linspace(start,stop,num="no of samples"(default=50),dtype)
generates "num" numbers from start to stop(inclusive) that are evenly spaced
'''
np6 = np.linspace(10,20,5)
print(np6)

'''
max,min- self explanatory
argmin,argmax - index(row number for n dimensional arrays) of min,max values
'''
print(np6.min(),np6.max(),np6.argmin(),np6.argmax())
print(np4.argmax(),np4.argmin())

os.system("cls")
'''
random.rand(row,col) - random numbers(need not be int) rowxcol np array(UNIFORM DIST)
random.randn(row,col) - normal distribution
'''

np7 = np.random.rand(3)
print(np7)
'''
random.randint(lowerbound,high_bound,size=10 or (row,col))
size is no of numbers to be generated
'''
np7 = np.random.randint(1,10,7)
print(np7)

os.system("cls")
'''
reshape(row,col)
imp note: rowxcol = original size
'''
np8 = np7.reshape(7,1)
print(np8)

'''
convert any (np array)matrix into one row vector
ravel() - any changes here will change orig matrix(reference)
flatten() - any changes here will not make changes to original matrix (copy)
'''
np9 = np7.ravel()
np9[2] = 45
print(np9,np7)
np10 = np7.flatten()
np10[2] = 90
print(np10,np7)

'''
transpose(np)
self explanatory
'''
np11 = np.transpose(np7) 
np11 = np7.T#does the same thing as above
print(np11)
'''
concatenate((np1,np2),axis=0(default) or 1(col wise concatenation))
dimensions of np's shud be same
'''
np8 = np.arange(4).reshape(2,2)
np9 = np.arange(4).reshape(2,2)
np12 = np.concatenate((np8,np9))#concatenates row wise, first np8 then followed by np9
print(np12)
np12 = np.concatenate((np8,np9),axis=1)#col wise concatenate
print(np12)
'''
split(np,num of cuts,axis=0 or 1(col wise))
splits np into num arrays row wise
num must be size/2
'''
os.system("cls")
np20 = np.arange(9).reshape(3,3)
print(np20)
np14 = np.split(np20,3)
print(np14)
np15 = np.split(np20,3,axis=1)
print(np15)
'''
unique(np,return_counts=True(default=False))
returns a row vector with all unqiue value in np array 
if ret_count is true along with above row vector it also returns a row vector with counts of unique values
'''
np16 = np.unique(np15,return_counts=True)
print(np16)

#Arithmetic operations
arr = np.arange(0,10)
arr1 = arr + arr
print(arr1) #addn
arr = np.arange(0,10)
arr1 = arr-arr
print(arr1)
arr = np.arange(0,10)
arr1 = arr*arr
print(arr1)
arr = np.arange(1,10)
arr1 = arr/arr
print(arr1)
arr = np.arange(1,10)
arr1 = arr%arr
print(arr1)
#Supports all mathematical functions
arr = np.arange(0,10)
arr1 = np.sqrt(arr)
print(arr1)
arr = np.arange(0,10)
arr1 = np.exp(arr)
print(arr1)
arr = np.arange(0,10)
arr1 = np.sin(arr)
print(arr1)
arr = np.arange(1,10)
arr1 = np.log(arr)
print(arr1)
#Conditional statements
arr = np.arange(0,10)
arr2 = arr>4 #array same dimensions as arr but only boolean values satisfying the condition
print(arr2)
arr = np.arange(0,10)
print(arr[arr%2==0]) #if used returns row vector of values(not booleans or not results after calculation) satisfying the condition
