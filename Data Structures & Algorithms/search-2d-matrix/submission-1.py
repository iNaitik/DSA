class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x =0
        while x < len(matrix):
            l =0
            r = len(matrix[x])-1
            while l <= r:
                mid = (l+r)//2
                if matrix[x][mid] > target:
                    r = mid -1
                elif matrix[x][mid] < target:
                    l = mid + 1
                else:
                    return True
            x += 1
        return False