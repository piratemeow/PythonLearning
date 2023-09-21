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
num = num+name # This will create a new list and assign it to num variable 
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

stri.sort(key = str.lower) # this will change the stri list


new_item=sorted(stri,key=str.lower) # this will create a sorted list from stri list but wont change the stri list


lis = [1+2, 'a'*4 , 'gekko'] # this will create a list of 3 items

print(lis) # [3, 'aaaa', 'gekko']

#Splicing   
liss = lis[1:2] # this will create a list of 1 item the staring index is included but the ending index is not.
print(liss) # ['aaaa'] 

del lis[1] # this will delete the item at index 1
lis2 = lis[:] # this will copy the list to another list
lis2 = lis # this will copy the list to another list but if we make any changes to lis2 it will reflect in lis also. Cause it only copies the reference of the list not the list itself

lis2 = list(lis) # This will copy the lis elements to lis2 and will not refernce to lis


# Some methods of list

# append() - Adds an element at the end of the list
# clear() - Removes all the elements from the list
# copy() - Returns a copy of the list
# count() - Returns the number of elements with the specified value
# extend() - Add the elements of a list (or any iterable), to the end of the current list
# index() - Returns the index of the first element with the specified value
# insert() - Adds an element at the specified position
# pop() - Removes the element at the specified position
# remove() - Removes the item with the specified value
# reverse() - Reverses the order of the list
# sort() - Sorts the list
# The list() Constructor - It is also possible to use the list() constructor to make a new list.

