from array import *


#1 create an array and  traverse
arr1=array('i',[5,9,10,11])
for i in arr1:
    print(i)

#2 access individual elements through indexes
print("Step 2")
print(arr1[3])

#3 append any value to the array
print("Step 3")
arr1.append(7)
print(arr1)

#4 insert
print("Step 4")
arr1.insert(0,20)
print(arr1)


#5 extend
print("Step 5")
arr2=array('i',[8,9,10])
arr1.extend(arr2)
print(arr1)

#6 add items from list to array 
print("Step 6")
templist = [3,5,9]
arr1.fromlist(templist)
print(arr1)
#7 remove any array element
print("Step 7")
arr1.remove(10) #removes the first 10
print(arr1)

#8 remove last array element
print("Step 8")
arr1.pop()
print(arr1)

#9 fetch any element through its index
print("Step 9")
print(arr1.index(5))

#10 reverse an array
print("Step 10")
arr1.reverse()
print(arr1)

#11 get array buffer information
print("Step 11")
print(arr1.buffer_info())

#12 check number of occurences of an element
print("Step 12")
print(arr1.count(9))

#13 convert array to string and string to array
print("Step 13")
strTemp=arr1.tobytes()
print(strTemp)
ints = array('i')
ints.frombytes(strTemp)
print(ints)

#14 convert array to python list
print("Step 14")
print(arr1.tolist())

#15 slice elements from an array
print("Step 15")
print(arr1[1:5])
print(arr1[2:])
print(arr1[:4])
print(arr1[:])