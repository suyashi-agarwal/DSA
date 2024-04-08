''' Lists : 1. holds an ordered collection of items
            2.can have different data types
            3. mutable - can change order/update
''' 

#Creating a list
lst=[]
lst1=['apple','orange','banana']
lst2=[1,2,'hey',[1,2]]
print(lst,lst1,lst1)

#Accessing / traversing
shoppinglist=['milk','bread','butter']
print(shoppinglist[0]) #0 is the first index
print(shoppinglist[-1]) # -1 is the first index

for i in shoppinglist:
    print(i)

for i in range(len(shoppinglist)):
    shoppinglist[i]= shoppinglist[i] + '+'
    print(shoppinglist[i])

empty =[]
for i in empty:
    print("I am empty")



#checking existence of an element in the list
shoppinglist=['milk','bread','butter']
print('bread' in shoppinglist)

#updation
mylist =[2,5,6,7,8]
mylist[2] = 10
print(mylist)
#O(1) - TIME AND SPACE COMPLEXITY

#INSERTION
mylist =[2,5,6,7,8]
#1.any position O(n)
mylist.insert(0,1)
print(mylist)
mylist.insert(3,10)
print(mylist)

#2.End O(1)
mylist.append(40)
print(mylist)

#3.Add another list O(n)
newlist=[10,11,12,13,14]
mylist.extend(newlist)
print(mylist)

#SLICING
lst = [3,4,5,5]
print(lst[:2])
print(lst[2:])
print(lst[1:2])
print(lst[:])

#updating multiple elements
lst[0:1]=['apple','orange']
print(lst)

#DELETION (space : O(1))
list1=['a','b','c','d','e','f']
list1.pop()
print(list1)
print(list1.pop()) #pop function returns the value of the deleted value also (o(n))

del list1[1:2] #o(n)
print(list1)
del list1[0]
print(list1)

list1.remove('c') #o(n)
print(list1)


#SEARCHING

#1.Using in operator
searchlist=[2,5,6,7,9]
target=5
'''if target in searchlist:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")'''

#2.#Linear search T : O(n)  S: O(1)
searchlist=[2,5,6,7,9]
def linearSearch(list_s, target_s):
    for i, value in enumerate(list_s):
        if value == target_s:
            return i
    return -1

print(linearSearch(searchlist,target))

#List operations/functions

'''
1. concatenation : + operator
2. repeat elements in the list : * operator
3. count number of elements in the list : len()
4. highest and lowest value in the list :max() and min()
5. sum of elements : sum()

'''

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c = a + b
print(c)

a=[1,2,3,4,5]
a = a*2
print(a)

print(len(a))

print(max(a))
print(min(a))

print(sum(a))

print(sum(a)/len(a)) #average

#excercise: optimize the given code using list functions:
'''
total = 0
count = 0
while(True):
    inp = input("Enter a number: ")
    if inp == 'done' : break
    value=float(inp)
    total += value
    count += 1
    average = total/count

print('Average is:', average)
'''


list = []
while(True):
    inp = input("Enter a number: ")
    if inp == 'done' : break
    value=float(inp)
    list.append(value)
average=sum(list)/len(list)

print('Average is :',average)






