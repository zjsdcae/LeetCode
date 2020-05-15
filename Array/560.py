def subarraySum(nums,k):    
    res, length = 0,len(nums)
    pre = [0]*(length+1)
    for i in range(1,length+1):
        pre[i] = pre[i-1]+nums[i-1]
    for m in range(1,length+1):
        for n in range(m,length+1):
            if pre[n] - pre[m-1] == k:
                res += 1
    return res

    # for i in range(length+1):
    #     for j in range(i,length+1):
    #         if nums[i:j] == []:
    #             continue
    #         if sum(nums[i:j]) == k:
    #             res += 1
    # return res

    #     if nums[i] == k:
    #         res += 1
    #     rev = k - nums[i]
    #     j = i+1 
    #     while j < length:
    #         if nums[j] == rev:
    #             res += 1
    #         rev -= nums[j]
    #         j += 1
    # return res

print(subarraySum([0,0,0,0,0,0,0,0,0,0],0))

