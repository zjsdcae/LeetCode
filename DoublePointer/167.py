class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i,v in enumerate(numbers):
            if v in dic:
                return [dic[v]+1,i+1]
            else:
                dic[target-v] = i