num = [1,2,'helllo',4,True]

print(len(num))
print(num)
print (num[2])

name = ['micheal','jordan']
print(len(name))
print('micheal' in name)

num.append(12) #To add an object to the list
print(num[-1])

# The ways to combine two lists together
num2 = num
num = num+name
print(num)
print(num2)
num2.extend([1,2,3])

dogs = [1,2,3,4,5,6]
print(len(dogs))
dogs.remove(1) # To remove an item from the list

dogs.remove(dogs[0])  # To remove an item from the list
print(dogs[0])


dogs.pop() # Removes the last item from the list

print(dogs[-1])


items= ['sadf','fad',1,12,34,54]

items.insert(0,0) #To insert item in a place of a list
items[0:0]=["he",'she']
items = [4,1,2,0,6]
itemcopy = items
print(items)
items.sort()
print(itemcopy) # Here the the itemcopy will also change

# to copy a list to another list
item = [0,35,6,6,7]
item2 = item[:] 
# now if i make any changes to item it won't reflect in item2


stri = ['1','b','fss']
#while sorting the function gives the capital letter lower value to improve this 

stri.sort(key = str.lower)


new_item=sorted(stri,key=str.lower) # this will create a sorted list from stri list but wont change the stri list




