# #For and while loop
# condition = True

# while condition==True:
#     print("The condition is true")
#     condition = False

# count = 0
# while count<10:
#     print(count)
#     count+=1

# while count:
#     print(count)
#     count-=1

items = [10,11,12,13]

for i in items:
    print(i)

print("Printing the items of the dictionary ")

dic = {1:2,'imran':'rahman'}

for i in dic: # This will print the key values 
    print(i)

for i in dic: # this will print the values
    print(dic[i])

for index,val in enumerate(items):
    print(index,val)



dic = {1:2,3:4}
for key,value in dic.items(): # items() returns a list of tuples as a view object of the dictionary that is iterable
    print(key,value)

arr = [[1,2,3],[4,5,6],[7,8,9]]
for b in arr:
    print(b[2])