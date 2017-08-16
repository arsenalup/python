def fib_func(num):
    a = 0
    b = 1
    for i in range(num):
        a, b = b, a+b
    return a

def fib_with_num(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a+b

def fib_with_bound(bound):
    a = 0
    b = 1
    while a <= bound:
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    # for i in range(10):
    #     print(fib_func(i))

    # for i in fib_with_num(10):
    #     print(i)
    #
    for i in fib_with_bound(100):
        print(i)
