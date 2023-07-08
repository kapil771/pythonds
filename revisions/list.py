list1 = [1,2,3,"edureka"]
print(list1)

print('========== Add ==============')
#append, extend, insert
list1.append((2,0))
print(list1)
list1.extend((4,9))
print(list1)
list1.insert(3,'example')
print(list1)

# print('========== Delete ==============')
#del, remove, pop
# del list1[3]
# print(list1)
# a = list1.pop(4)
# print(a)
# list1.remove(2)
# print(list1)

print('========== Display ==============')
print(list1)
print(list1[0:2])
print(list1[0:8:2]) # skip 1 element
print(list1[::-1])