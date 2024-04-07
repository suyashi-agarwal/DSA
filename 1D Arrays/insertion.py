import array

# .insert(index,element)
my_arr2 = array.array('i',[1,2,3,4])  
my_arr2.insert(0,7) #beginning
my_arr2.insert(2,8) #in between
my_arr2.insert(4,7) #end
print(my_arr2)

#Time complexity : 0(N) [depends on the number of elements that have to be shifted right,in this case when we insert the element in the beginning,all elements have to be shifted]
#Space complexity : O(1)[only 1 block of space]