def twoSum(nums, target):
    # hashMap = {}
    # for i in range(len(nums)):
    #     if(nums[i] in hashMap):
    #         return ([i,hashMap[nums[i]]])
    #     else:
    #         hashMap[target-nums[i]] = i

    d = {}
    for i, num in enumerate(nums):
        if num in d:
            return [d.get(num),i]
        else:
            d[target-num] = i