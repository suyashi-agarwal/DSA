import numpy as np

a=np.array([[1,2,3,4],[4,5,6,7],[3,6,8,9],[1,2,5,8]])
print(a)

#inserting a row
b=np.insert(a,1,[[4,2,5,4]],axis=0)
print(b )

#inserting a column
b=np.insert(a,2,[[4,2,5,4]],axis=1)
print(b )

#inserting at the end
b=np.append(a,[[2,1,2,1]],axis=0)
print(b)



