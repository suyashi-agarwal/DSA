import numpy as np

a=np.array([[1,2,3,4],[4,5,6,7],[3,6,8,9],[1,2,5,8]])
print(a)


#LINEAR SEARCH
def searchElement(array,ele):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == ele :
                print("The value is located at index " + str(i) +""+ str(j))
    return "The element is not found"

searchElement(a,9)

#O(mn)
