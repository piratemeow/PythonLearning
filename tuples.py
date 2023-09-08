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

tup2 = (1,2),(2,3),(3,4) # This is a tuple of tuples
print(tup2)
print(tup2[0])

dic = dict(tup2) # This will convert the tuple of tuples to a dictionary
print(dic[1]) # This will return the value of the key 1 as dictionary can not be accessed with index

dic2 = {'a':1,'b':2,'c':3}
tup3 = tuple(dic2.items()) # This will convert the dictionary to a tuple of tuples
print(tup3)
print(tup3[0]) # This will return the value of the key 0 as tuple of tuples can be accessed with index
tup4 = tuple(dic2.values()) # This will convert the dictionary to a tuple of values 
print(tup4)
tup5 = tuple(dic2.keys()) # This will convert the dictionary to a tuple of keys tuple(dic2) will also do the same
print(tup5)
