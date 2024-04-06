from array import *

my_arr1 = array('i',[1,2,3,4,6,10])

my_arr1.remove(2)
print(my_arr1)

#after deletion all the elements shift to the left since array has to be stored in a contigous manner

#T(n) = O(N)
#S(n) = O(1)
