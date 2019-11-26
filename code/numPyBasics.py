import numpy as np
# Why numpy? -> numpy much faster than lists 
# numpy libraries vs lists
# numpy int size can be altered
# for a normal int we deal with object value object type reference value and size
# since numpy uses less memory we are dealing with less stuff
# no type checking when iterating through objects
# contiguous memory
a = np.array([[1, 2, 3],[4, 5, 6]])
print(a.ndim)
print(a.shape)
a = a.astype('int16')
print(a.dtype)
print(a.nbytes)
print(a.size*a.nbytes)
print(a[0, :])
b = np.zeros((2,3))
print(b)
#np.full
#np.array to repeat arrays