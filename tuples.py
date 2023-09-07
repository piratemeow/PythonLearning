"""Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).
    Once created their values can not change.
"""

tup = (1,2,3,4,5)

print(type(tup))

#Conversion to list

lis = list(tup)
print(lis)

# They can be accessed with index
a = tup[-1] # This will return the last element of the tuple
print(a)

liss = [(1,2,3),(4,5,6)]
print(liss)
print(liss[0]) # This will return the first tuple
print(liss[0][1]) # This will return the second element of the first tuple
for i in enumerate(tup):
    print(i)