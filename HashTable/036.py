class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])

                    idx = i // 3 * 3 + j // 3 
                    if num in column[j] or num in row[i] or num in box[idx] :
                        return False
                    
                    column[j].add(num)
                    row[i].add(num)
                    box[idx].add(num)
        
        return True