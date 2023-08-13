set1 = {1,2,3,4,4,4}
print(set1)

# new element added
set1.add(5)
print(set1)

# union(), intersection(), difference(), symmertic_difference()
# Difference: Elements present on one set, but not on the other. 
# Symmetric Difference: Elements from both sets, that are not present on the other.
set2 = {3,4,5,6}
print('union:::::',set1.union(set2))
print('intersection:::::',set1.intersection(set2))
print('difference:::::',set1.difference(set2))
print('symmetric_difference:::::',set1.symmetric_difference(set2))