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

items = [1,2,3,5]

for i in items:
    print(i)

print("Printing the items of the dictionary ")

dic = {1:2,'imran':'rahman'}

for i in dic: # This will print the key values 
    print(i)

for i in dic: # this will print the values
    print(dic[i])