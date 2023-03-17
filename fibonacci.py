def fib(x):
    if x <= 2:
        return x
    while x > 2:
        return fib(x-2) + fib(x-1)
    

print([fib(i) for i in range(0,15)])
