# stores pairs

dic = {1:2,'age':9,3:'hehe'}

#to access use name[keyvalue]

print(dic['age'])

dic['age']=12
#dictionary.get(key) will get you the value of the key
# It will print none if the key does not exist
print(dic.get('age'))
#If the function is to return a certain value if the given key does not exist
print(dic.get('color','black'))

#dictionary.pop(key) will delete the key and the value
# The function alse returns the value
dic.pop(1)
print(len(dic))

#dictionary.popitem() will delete the last key value pair

print('hehe' in dic)

# .keys() will print the keys
# .items() will print the items
 
#to delete an key value pair

del dic['age']

# To copy a dictionary

dic2 = dic.copy()