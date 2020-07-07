class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','{':'}','[':']'}
        left = {'(','{','['}
        length = len(s)
        if length%2 == 1:
            return False
        tempStack = []
        for i in range(length):
            if s[i] in left:
                tempStack.append(s[i])
            else:
                if tempStack == []:
                    return False
                top = tempStack.pop()
                if dic[top] == s[i]:
                    continue
                else: 
                    return False
        if len(tempStack) != 0:
            return False
        return True
