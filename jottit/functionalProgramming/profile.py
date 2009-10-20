
import time

def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def profile(f):
    f.count = 0
    def g(x):
        if f.count == 0:
            t1 = time.time()
        f.count += 1
        value = f(x)
        f.count -=1
        if f.count == 0:
            t2 = time.time()
            print 'time taken:', t2-t1
        return value
    return g

if __name__ == "__main__":
    fib = profile(fib)
    print fib(20)
    
