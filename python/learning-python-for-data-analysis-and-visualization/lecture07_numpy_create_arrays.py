import numpy as np

# create array from list
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print(my_array1)
# [1 2 3 4]

# combine two lists
my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]

# create a multidimensional array a.k.a matrix
my_array2 = np.array(my_lists)
print(my_array2)
'''
[[ 1  2  3  4]
 [11 22 33 44]]
'''

print(my_array2.shape)
# (2, 4)

print(my_array2.dtype)
# int64

# special case arrays
# zeros
print(np.zeros(5))
# [ 0.  0.  0.  0.  0.]

# ones
print(np.ones([5, 5]))
'''
[[ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]
 [ 1.  1.  1.  1.  1.]]
'''

# empty - equivalent to zeros
print(np.empty(4))
# [ 0.  0.  0.  0.]

# identity matrix
print(np.eye(4))
'''
[[ 1.  0.  0.  0.]
 [ 0.  1.  0.  0.]
 [ 0.  0.  1.  0.]
 [ 0.  0.  0.  1.]]
'''

# generate random arrays
print(np.arange(5))
# [0 1 2 3 4]
print(np.arange(5, 20, 4))
# [ 5  9 13 17]
print(np.arange(20))
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(np.arange(20).reshape(4, 5))
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
'''
