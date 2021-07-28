def fun(string):
    currentLongest = [0,1]
    for i in range(1,len(string)):
        odd = getLongestPalindrome(string,i-1,i+1)
        even = getLongestPalindrome(string,i-1,i)
        longest = max(odd,even,key = lambda x:x[1]-x[0])
        currentLongest = max(longest,currentLongest,key = lambda x:x[1]-x[0])
    return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindrome(string,indexLeft,indexRight):
    while indexLeft >= 0 and indexRight < len(string):
        if string[indexLeft] != string[indexRight]:
            break
        indexLeft -= 1
        indexRight += 1
    return string[indexLeft+1,indexRight]

print(fun("abcddcba"))
