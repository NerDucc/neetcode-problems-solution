class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m*n -1
        while lo <= hi:
            mid = (lo+hi)//2
            r, c = mid//n, mid%n
            mid_val = matrix[r][c]
            if mid_val == target:
                return True
            elif mid_val > target:
                hi = mid -1
            else:
                lo = mid + 1
        return False