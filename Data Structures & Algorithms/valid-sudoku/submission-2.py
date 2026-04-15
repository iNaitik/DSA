class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        for i in board:
            hashmap.clear()
            for j in i:
                if j == '.':
                    continue
                if j in hashmap:
                    return False
                else:
                    hashmap[j] = 1
        for i in range(9):
            hashmap.clear()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in hashmap:
                    return False
                else:
                    hashmap[board[j][i]] = 1
        starts = [(0,0),(0,3),(0,6),
                    (3,0),(3,3),(3,6),
                    (6,0),(6,3),(6,6)]
        for i,j in starts:
            hashmap.clear()
            for row in range(i,i+3):
                for column in range(j,j+3):
                    if board[row][column] == '.':
                        continue
                    if board[row][column] in hashmap:
                        return False
                    else:
                        hashmap[board[row][column]] = 1
        return True
    
