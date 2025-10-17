class Solution:
    def mySqrt(self, x: int) -> int:
        # using the binary search
        if x < 2:
            return x
        left , right = 0, x // 2
        while left <= right:
            mid = (left + right ) // 2
            square = mid * mid 
            if square == x:
                return mid
            elif square < x:
                # search right side 
                left = mid + 1
            else:
                # search the left side 
                right = mid - 1 
        return right
    
# https://www.youtube.com/watch?v=W7S94pq5Xuo
# we can also implement Newton's Method.


sol = Solution()
print(sol.mySqrt(1)) # 1
print(sol.mySqrt(0)) # 0
print(sol.mySqrt(2)) # 1
print(sol.mySqrt(5)) # 2
print(sol.mySqrt(9)) # 3
print(sol.mySqrt(10)) # 3
print(sol.mySqrt(25)) # 5