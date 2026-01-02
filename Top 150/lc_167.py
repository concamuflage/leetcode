class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left +=1
            elif numbers[left] + numbers[right] > target:
                right -=1
            else:
                return [left+1,right+1]

sol = Solution()
print(sol.twoSum(numbers = [2,7,11,15], target = 9)) # [1,2]
print(sol.twoSum(numbers = [2,3,4], target = 6)) # [1,3]
print(sol.twoSum(numbers = [-1,0], target = -1)) # [1,2]