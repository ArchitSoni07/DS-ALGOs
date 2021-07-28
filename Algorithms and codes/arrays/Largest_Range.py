def fun(array):
    bestRange = []
    nums = {}
    longestLength = 0
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
          continue
        nums[num] = False
        currentLength = 1
        left = num-1
        right = num+1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left+1,right-1]
    return bestRange

print(fun([23,78,45,26,98,75,41,88,45,89,90,122,91,55,92,93]))

        