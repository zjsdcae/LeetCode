class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i,j,board,words):
            res = False
            if len(words) == 0: return True 
            if not 0 <= i < leni or not 0 <= j < lenj: return False
            if board[i][j] != words[0]: return False
            temp,board[i][j] = board[i][j],'#'
            res = search(i-1,j,board,words[1:]) or search(i+1,j,board,words[1:]) or search(i,j-1,board,words[1:]) or search(i,j+1,board,words[1:]) 
            board[i][j] = temp
            return res 

        leni,lenj = len(board),len(board[0])
        for i in range(leni):
            for j in range(lenj):
                if board[i][j] == word[0]:
                    if search(i,j,board,word): return True 
        return False 

