def fun(array):
    lefti = 0
    righti = len(array)-1
    while lefti<righti:
        if array[lefti] != array[righti]:
            return False
        lefti += 1
        righti -= 1
    return True

print(fun(['a','b','c','d','c','b','a']))