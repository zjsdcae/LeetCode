class Solution:
    def findClosest(self, words, word1, word2):
        length = len(words)
        dis = length
        matchWord = [word1, word2]
        i = 0
        while i < length-1:
            j = i + 1
            if words[i] in matchWord:
                while words[j] not in matchWord:
                    if j == length-1:
                        break
                    j += 1
            else:
                i += 1
                continue
            if words[j] not in matchWord and j == length-1:
                return dis
            elif words[j] in matchWord and words[i] in matchWord:
                if words[j] == words[i]:
                    i = j
                else:
                    if j - i < dis :
                        dis = j - i
                    i = j
        return dis