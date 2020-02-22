#homework5 - Basic

import np as np
import numpy as np

#creating array
a = np.array([1, 22.4, 5, 35, 4, 6, 7,3, 8,40])
print ("Array between 0-40" , a)
print (a.ndim)
print (a.shape)
print (a.dtype)

# creating matrix
matrix = np.array([['a', 'b'], ['c', 'd'], [3, 3]])
print ("First matrix" , matrix)
print (matrix.dtype)
print (matrix.ndim)
print (matrix.shape)

numpy1 = np.arange(0,20)
print ("One dimension array using arrange" , numpy1)
numpr = np.random.rand(1,2)
print ("One dimension array using rand" , numpr)

numpy2 = np.zeros((2, 5))
print ("2 dimensions matrix using zeros" ,numpy2)
numpr2 = np.random.rand(2,2)
print ("2 dimensions matrix using rand", numpr2)

#reshape array

numpy7 = np.full((1, 20),  7).reshape(4,5)
print ("Reshape array", numpy7)

# create 6*6 matrix and reshape it

array6 = np.arange(36).reshape(6,6)
print ("6*6 reshaped array:" , array6)
print ("First element of 6*6 array", array6[0,1])
print ("last 2 rows of 6*6 array", array6 [4:6, :])
print ("Mid 2 rows", array6 [2:4, 2:4])
#middle = lambda array6: array6[len(array6)/4:len(array6)*3/4]
#print (middle)
print ("Sum of 6*6 array" , array6.sum(axis=0))
