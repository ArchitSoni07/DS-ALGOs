def fib(n):
    if n == 2:
        return 1
    if n == 1:
        return 0
    else:
        return fib(n-1)+fib(n-2)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def fib1(n,memoize = {1: 0 , 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib1(n-1,memoize)+fib1(n-2,memoize)
        return memoize[n]

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def fib2(n):
    array=[0,1]
    counter = 3
    while counter <= n:
        nextfib = array[0]+array[1]
        array[0] = array[1]
        array[1] = nextfib
        counter += 1
    return array[1] if n >1 else array[0] 

