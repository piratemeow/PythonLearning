def math(a,b):
    print('Would you like to add another number?')
    s=input()
    if s=='yes':
        c=int(input())
        def sum(c):
            ans = a+b+c
            return ans
        return sum(c)
        
    else:
        ans =a+b
        return ans
    

a = int( input())
b = int(input())
print(math(a,b))

def counter():
    count = 0
    def add():
        nonlocal count
        count+=1
        return count
    return add

x = counter()


print(x()) #1
print(x()) #2
print(x()) #3
print(x()) #4
#As the inner function does not call the outer count so every time it keeps the new count value