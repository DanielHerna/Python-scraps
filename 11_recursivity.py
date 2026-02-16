
#1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

''' Fibonacci 
0 1 1 2 3 5 8 12 20 ...

'''

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(3))


#3

def nat_sum(n):
    if n==0:
        return 0
    else:
        return n+nat_sum(n-1)

print(nat_sum(500))