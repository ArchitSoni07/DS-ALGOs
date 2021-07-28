# T  o(nlog(n))    S   o(1)

def fun(array,targetsum):
    array.sort()
    lefti = 0
    righti = len(array)-1
    while lefti < righti:
        if array[lefti]+array[righti] < targetsum:
            lefti += 1
        if array[lefti]+array[righti] > targetsum:
            righti -= 1
        else:
            return [array[lefti],array[righti]]
print(fun([3,5,-4,8,11,1,-1,6],10))