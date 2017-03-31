def fi(n):
    a=0
    b=1
    c=0
    for i in range(n-1):
        c=b
        b=a+b
        a=c
    return b
print fi(10)



def fib(n):
    if n==1 or n==2:
        print 1
    return fib(n-1)+fib(n-2)
print fib(10)