from array import *

my_arr1 = array('i',[1,2,3,4])

def linear_search(array,ele_to_be_searched):
    for i in range (len(array)):            #T(N)=0(N)   S(N)=0(1)
        if array[i] == ele_to_be_searched:
            return i
    return -1

print(linear_search(my_arr1, 3))
