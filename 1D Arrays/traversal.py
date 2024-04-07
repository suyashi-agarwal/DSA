from array import *

my_arr1 = array('i',[1,2,3,4])
my_arr2 = array('d',[1.3,2.3,3.5,4.9])

def traverseArray(array):  # t(n) : O(N)
    for i in array:         #S(n) : O(1)
        print(i)

traverseArray(my_arr1)
traverseArray(my_arr2)

