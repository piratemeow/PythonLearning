#map is function that execuutes a function for every
#element of a list and returns a new list

number = [1,2,3,4]

def mul(a):
    return a*2

result = map(mul,number)
#other way to do it
x = lambda a:a*2
result = map(x,number)

#other way to do it 
result = map(lambda a:2*a,number)

for i in result:
    print(i)

# if we want to print the result here we must cast it to a list first

print(list(result))


#filter is function that execuutes a function for every
#element of a list and if an element return true then it is added
# to the list, otherwise not and returns a new list

item = [1,2,3,4,5,6,7,8,9,10]

answer = filter(lambda a : a%2==0,item)

print(list(answer)) 