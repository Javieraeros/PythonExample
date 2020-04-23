import time

dictionary = {
    "name": "Perico",
    "surname": "Palotes",
    "job": "Programmer",
    "hobby": "music",
    "": ""
}


def print_times(func, *args):
    begin_time = time.time()
    func(args)
    end_time = time.time()
    print(end_time - begin_time)


def fib(n: int):
    """Function to calculate the first n numbers of fibonacci sequence"""
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()
