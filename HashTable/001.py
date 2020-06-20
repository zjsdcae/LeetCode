def twoSum( nums,target ):
    dic = {}
    for idx, v in enumerate(nums):
        if v in dic:
            return [dic[v],i]
        dic[target-v] = idx

