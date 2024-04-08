import numpy as np

a=np.array([[1,2,3,4],[4,5,6,7],[3,6,8,9],[1,2,5,8]])
print(a)

def accessElements(array,rowIndex,columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print('incorrect index')
    else:
        print(array[rowIndex][columnIndex])

accessElements(a,0,0)

