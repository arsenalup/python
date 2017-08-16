import threading
import sched
import time


def simple_timer():
    def say_hello(word):
        print('hello', word)
    my_timer = threading.Timer(1.0, say_hello, ['python'])
    my_timer.start()


def loop_use_threading():
    def say_hello(word):
        print('hello', word)
        my_timer = threading.Timer(1.0, say_hello, ['python'])
        my_timer.start()
    my_timer = threading.Timer(1.0, say_hello, ['python'])
    my_timer.start()

def loop_use_sched():
    def say_hello(sc, word):
        print('hello', word)
        # sc.enter(1.0, 1, do_something, [sc, 'python'])
    my_sc = sched.scheduler(time.time, time.sleep)
    my_sc.enter(1.0, 1, say_hello, [my_sc, 'python'])
    my_sc.run()


if __name__ == '__main__':
    # simple_timer()
    # loop_use_sched()
    loop_use_threading()
