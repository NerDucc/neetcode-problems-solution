class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0 , x
        while l <= r:
            mid = (r+l)//2
            ans = mid*mid
            if ans == x:
                return mid
            elif ans > x:
                r = mid-1
            else:
                l = mid+1
        return r