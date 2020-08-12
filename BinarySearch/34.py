class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        l,r,mid = 0,len(nums)-1,-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l > r:
            return res
        ll,lr = 0,mid
        while ll <= lr:
            midl = (ll+lr) >> 1
            if nums[midl] == target:
                lr = midl - 1
            else:
                ll = midl + 1
        rl,rr = mid,len(nums)-1
        while rl <= rr:
            midr = (rl+rr) >> 1
            if nums[midr] == target:
                rl = midr + 1
            else:
                rr = midr - 1
        return [ll,rr]