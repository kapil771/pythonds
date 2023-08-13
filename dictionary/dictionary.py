dict1 = {1:'Javascript',2:'Java'}
print(dict1)

dict1[1]='Python'
print(dict1)

dict1[3] = 'Ruby'
print(dict1)


# del
# print(dict1.pop(1))
# del dict1[1]
print(dict1.popitem())
print(dict1)

# print(dict1.keys())
# print(dict1.values())
print(dict1.items())