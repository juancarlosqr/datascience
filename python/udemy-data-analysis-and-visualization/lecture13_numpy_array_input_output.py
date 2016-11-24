import numpy as np

arr = np.arange(5)
print(arr)
# [0 1 2 3 4]

# save
np.save('my_arr', arr)

arr = np.arange(10)
print(arr)
# [0 1 2 3 4 5 6 7 8 9]

# load
my_arr = np.load('my_arr.npy')
print(my_arr)
# [0 1 2 3 4]

# multiple arrays - np.savez
my_arr2 = np.arange(6)
np.savez('ziparray.npz', x=my_arr, y=my_arr2)

archive = np.load('ziparray.npz')
print(archive['x'])
# [0 1 2 3 4]
print(archive['y'])
# [0 1 2 3 4 5]

# text file
arr = np.arange(6).reshape(2,3)
print(arr)
'''
[[0 1 2]
 [3 4 5]]
'''
np.savetxt('my_text_array.txt', arr, delimiter=',')

new_arr = np.loadtxt('my_text_array.txt', delimiter=',')
print(new_arr)
'''
[[ 0.  1.  2.]
 [ 3.  4.  5.]]
'''
