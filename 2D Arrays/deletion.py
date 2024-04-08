import numpy as np

a=np.array([[1,2,3,4],[4,5,6,7],[3,6,8,9],[1,2,5,8]])
print(a)


b=np.delete(a,1,axis=0)
print(b)

#Creates an new array excluding the row or column to be deleted.
#O(mn)
