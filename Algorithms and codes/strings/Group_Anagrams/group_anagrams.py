# Time = O(w*n*log(n) + n*w*log(w))   
#         
# w->words n->len(longestWord) ;)
#
# SPACE = O(wn)


def fun(words):

    if len(words) == 0:
        return []

    sortedWords = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x:sortedWords[x])

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]

    for index in indices:
        word  = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue

    
        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result

print(fun(["yo","act","flop","tac","cat","oy","olfp"]))



#### BETTER ################################################################################

# Time ->   O(w*n*log(n))
# Space ->  O(wn)  

def fun1(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

print(fun1(["yo","act","flop","tac","cat","oy","olfp"]))