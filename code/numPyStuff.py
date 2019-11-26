import numpy as np
my_array = np.array([3, 4, 5, 6, 7, 99])
str_array = my_array.astype(str)
two_dim_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.mean(two_dim_arr, axis=1))
print(two_dim_arr[0, ::-1])
np.savetxt('2darr.csv', two_dim_arr, delimiter=',')
print(np.genfromtxt('2darr.csv', delimiter=','))