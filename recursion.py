#Works just as it would work in any other language
#Nothing new here



# Recursive Fucntion to find factorial 

def fac(n):
    if (n==1):
        return 1
    
    return n*fac(n-1)

# Recursive Function to find fibonacchi number 

def fibo(n):
    if (n<=2):
        return 1
    return fibo(n-1)+fibo(n-2)

# Recursive function for linear search

def ser(i,val, lis):
    if (i>=len(lis)):
        return -1
    if (val==lis[i]):
        return i
    return ser(i+1,val,lis)

print(fac(20))

print(fibo(6))

lis = [1,2,3,4,5]

print(ser(0,3,lis)) # prints the index of the value found in the list