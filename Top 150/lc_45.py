
# class Solution:
#     def jump(self, nums: list[int]) -> int:
#         dic = [-1]*len(nums)
#         dic[0] = 0
#         if len(nums) == 1:
#             return 0
#         for index,num in enumerate(nums):
#             if dic[index] != -1 : # this number is reachable
#                 current_step = dic[index]
#                 min_step = current_step + 1 # current minimum step
#                 for index_2 in range(num):
#                     result = index + index_2 + 1
#                     if result < len(nums) and dic[result] != current_step : # valid index
#                         dic[result] = min_step
#         return dic[-1]
#
class Solution:
    def jump(self, nums):
        # this method is the same as the previous one
        # instead of using an array, it uses pointers end and farthest.

        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        end = 0          # end of current layer
        farthest = 0     # farthest index within next layer

        # no need to step on the last index; once we cross it, we're done
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:          # finish current jump's coverage
                jumps += 1
                end = farthest
                if end >= n - 1:  # already can reach/overreach last index
                    break
        return jumps

sol = Solution()
print(sol.jump([2])) # 0
print(sol.jump([1,1])) # 1
print(sol.jump([2,3,1,1,4])) #2
print(sol.jump([2,3,0,1,4])) #2


