def fun(one,two,three):
    if len(three) != len(two)+len(one):
        return False
    return areInterwoven(one,two,three,0,0)

def areInterwoven(one,two,three,i,j):
    k = i+j
    if k == len(three):
        return True
    
    if i < len(one) and one[i] == three[k]:
       if areInterwoven(one,two,three,i+1,j):
           return True

    if j < len(two) and two[j] == three[k]:
       return areInterwoven(one,two,three,i,j+1)

    return False

# Time      -->     O( 2^(n+m) )
# Space     -->     O(n+m)

###################################################################################

print(fun("aaa","faaaa","aaafaaaa"))



def fun1(one,two,three):
    if len(three) != len(two)+len(one):
        return False
    OneTwo = one+two
    TwoOne = two+one
    if OneTwo == three or TwoOne == three:
        return True