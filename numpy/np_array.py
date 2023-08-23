import numpy as np

lst = [1, 2, 3, 4]
result = np.array(lst)
# print(lst)
print(result)
print(type(result))
print(result.shape)


lst1 = [10, 22, 33, 44, 15]
lst2 = [21, 31, 42, 45, 56]
lst3 = [33, 42, 51, 46, 37]
twodarr = np.array([lst1, lst2, lst3])
print('twodarr::::', twodarr)
# print(type(twodarr))
print(twodarr.shape)
print('=======================================')
print(result[3])
print('=======================================')
result[3] = 5
print(result)
print('=======================================')
print(result[1:])
print('=======================================')
print('All Elements::::', result[-2])
print('=======================================')
print('All Elements::::', result[::])
print('=======================================')
print('Reverse::::', result[::-1])
print('=======================================')
print(twodarr[1, :])
print('=======================================')
print(twodarr[1:, 1:3])
print('=======================================')
print(twodarr[:, 0:].shape)
