def fun(n,denoms):
    numOfCoins = [float("inf") for amount in range(n+1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount],1+numOfCoins[amount-denom])
    return numOfCoins[n] if numOfCoins[n] != float("inf") else -1

print(fun(6,[1,2,4]))
print(fun(7,[2,4]))

#Space O(n)
#Time O(nd) d->denoms n->target amount