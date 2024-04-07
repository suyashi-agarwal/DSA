from array import *

my_arr1 = array('i',[1,2,3,4])

#  user tries to access element that is out of bounds of the array ---> no element
# otherwise arrayname[index]

def AccessElements(array,index):   # T(n) = S(n)= O(1)
    if(index >= len(array)):    
        print("No element exists on that index") 
    else:
        print(array[index]) 

AccessElements(my_arr1,2)
AccessElements(my_arr1,4)
