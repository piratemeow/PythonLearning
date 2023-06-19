def hello(name, age):
    print("Hello " + name)
    print("Your age is " , age)



# name = input()
# age = input()

hello('imran',12)

# For the mutable data types the function call will be 
# similar to call by reference scheme in cpp that means any
# change in the function in the inside will reflect to the outside


# For the immutable data types the function call will be 
# similar to call by value scheme in cpp that means any
# change in the function in the inside will not reflect to the outside


def change (a,b):
   a=1
   b=1

a=12
b=12

change(a,b)
print(a,b)

# Returns multiple values
def sum(a,b):
    return "The sum is ", a+b

print(sum(a,b))


