list1 = [1,2,3,'edureka']
# list1.append(2)
list1.append((2,0))
list1.extend((3,9))
list1.insert(3,'example')
print(list1)

# del,pop(), remove()
del list1[3]
print(list1)
a = list1.pop(4)
print(a)
print(list1)
list1.remove(2)
print(list1)