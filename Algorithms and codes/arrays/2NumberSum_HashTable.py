def fun(array,targetsum):
    nums = {}
    for num in array:
        if targetsum-num in nums:
            return [targetsum-num,num]
        else:
            nums[num] = True
    return []

print(fun([3,5,-4,8,11,1,-1,6],10))

#O(n) T     O(n)  S