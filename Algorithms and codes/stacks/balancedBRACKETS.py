def split(word): 
    return list(word)

def balancedbrackets(mystring):
    oround = '('
    countor = 0

    osquare='['
    countos=0

    ocurly='{'
    countoc = 0

    cround=')'
    countcr=0

    csquare='}'
    countcs=0

    ccurly='}'
    countcc=0


    charArray = split(mystring)
    for i in charArray:
        if hex(id(i)) == hex(id(oround)):
            countor += 1
            return countor

        elif hex(id(i)) == hex(id(osquare)):
            countos +=1
            return countos

        elif hex(id(i)) == hex(id(ocurly)):
            countoc +=1
            return countoc

        elif hex(id(i)) == hex(id(cround)):
            countcr +=1
            return countcr

        elif hex(id(i)) == hex(id(csquare)):
            countcs +=1
            return countcs
        else:
            countcc +=1
            return countcc

    if countor==countcr and countcc==countoc and countcs==countos:
        return True
    else:
        return False



print(balancedbrackets("(([]{}))"))