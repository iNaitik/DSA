class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        for row in board:
            hashmap.clear()
            for val in row:
                if val == '.':
                    continue
                if val in hashmap:
                    return False
                hashmap[val] = 1

        for i in range(9):
            hashmap.clear()
            for j in range(9):
                val = board[j][i]
                if val == '.':
                    continue
                if val in hashmap:
                    return False
                hashmap[val] = 1

        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i ,j in starts:
            hashmap.clear()
            for row in range(i,i+3):
                for column in range(j,j+3):
                    val = board[row][column]
                    if val == '.':
                        continue
                    if val in hashmap:
                        return False
                    hashmap[val] = 1
        return True