import numpy as np

a=np.array([[1,2,3,4],[4,5,6,7],[3,6,8,9],[1,2,5,8]])
print(a)

def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseArray(a)
