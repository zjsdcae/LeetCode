# class Solution:
#     def replaceSpace(self, s: str) -> str:
#         res = ""
#         for char in s:
#             if char == " ":
#                 res += "%20"
#             else:
#                 res += char
#         return res
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace("","%20")