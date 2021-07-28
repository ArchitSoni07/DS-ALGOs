def productSum(array,m=1):
    sum =0
    for element in array:
        if type(element) is list:
            sum += productSum(element,m+1)
        else:
            sum += element
    return sum * m
