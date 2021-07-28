import math
array = ["a","b","c","d","c","b","a"]
count = 0
i=0
if len(array)%2 != 0:
    for i in range(0,len(array)):
        while i < math.floor(len(array)/2):
            if array[i] == array[len(array)-1-i]:
                count = count +1 
    if count == math.floor(len(array)/2):
            print("True")
if len(array)%2 == 0:
    for i in range(0,len(array)):
        while i < (len(array)/2):
            if array[i] == array[len(array)-1]:
                count = count +1 
    if count == math.floor(len(array)/2):
        print("True")
print("False")
