# class Solution:
#     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         lengthPop = len(popped)
#         if len(pushed) == 0:
#             return True
#         i,s = 0,[]
#         while pushed:
#             s.append(pushed.pop(0))
#             while s and s[-1] == popped[i] and i < lengthPop:
#                 s.pop()
#                 i += 1
#         length = len(s)
#         if length > 0:
#             while s and s[-1] == popped[i] and i < lengthPop:
#                 s.pop()
#                 i += 1
#         return True if not s else False

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lengthPop = len(popped)
        if len(pushed) == 0:
            return True
        i,s = 0,[]
        while pushed:
            s.append(pushed.pop(0))
            while s and s[-1] == popped[i] and i < lengthPop:
                s.pop()
                i += 1
        return not s