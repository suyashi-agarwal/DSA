# 1. using array module
# 2. using numpy

#1
import array
my_arr = array.array('i') # O(1)
print(my_arr)
my_arr2 = array.array('i',[1,2,3,4])  #Time and space complexity : O(N)
print(my_arr2)


#2
import numpy as np
np_arr = np.array([],dtype =int) #O(1)
print(np_arr)
np_arr2 = np.array([4,3,4,2,1])  #Time and space complexity : 0(N)
print(np_arr2)

