#写一个迭代器，生成前10个斐波拉契数。（前两个斐波拉契数是0和1）
#稍微改动一下，生成小于100的斐波拉契数。

class Fib_with_bound:
    def __init__(self, bound):
        self.bound = bound

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        next_num = self.a
        if next_num > self.bound:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        return next_num

    def nest(self):
        return self.__next__()


class Fib_with_num:
    def __init__(self, nums):
        self.nums = nums

    def __iter__(self):
        self.count = 0
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        self.count +=1
        next_num = self.a
        if self.count > self.nums:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return next_num

    def next(self):
        return self.__next__()

if __name__ == '__main__':
    fib = Fib_with_num(10)
    # print(type(fib))
    for i in fib:
        print(i)

    # fib2 = Fib_with_bound(100)
    # for i in fib2:
    #     print(i)
