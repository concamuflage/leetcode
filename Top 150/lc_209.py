# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         # best_ans stores the length of the shortest array within [0,right] range.
#         # as the index right move to the position n-1, it stores the global minimum.
#         # it is easy to understand the algorithm, but hard to implement
#         # because according to my train of thought, there are too many edge cases to consider.
#
          # By mistake, I covered cases when target is bigger than 1
          # this probably makes my code more convoluted than necessary.
#         if len(nums) == 1:
#             if nums[0] >= target:
#                 return 1
#             else:
#                 return 0
#
#
#         left = 0
#         right = -1
#         length = len(nums)
#         total = 0
#         ans = 0
#         best_ans = len(nums) # give it a bit number
#         while right < length - 1:
#             right += 1
#             ans = right - left + 1
#             total += nums[right]
#             if total >= target:
#                 while total - nums[left] >= target: # if the left element can be removed.
#                     total -= nums[left]
#                     left += 1
#                     ans -= 1
#                 best_ans = min(best_ans, ans)
#
#         # this case only happens when you add all the elements in the array and total still less than target.
#         # if the inner while loop is entered for only once, the total > target because
#         # at exit of the inner loop, in case total < total, the last removed element is added back
#         # so the total > target.
#         if total < target:
#             return 0
#         return min(best_ans,ans)


class Solution:
    # GPT answer
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        ans = float('inf') # this stores the answers

        for right, x in enumerate(nums):
            total += x
            # shrink while we still meet/exceed target

            # trace for [1,4,4] with target = 4
            #        0    0    inf
            # 0      0    1    inf
            # 1      0    5    inf
            # 1a     1    4     2
            # ib     2    0     1(correct answer) # total reduced to 0 and left pointer moved past right pointer.
            # 2      2    4
            # 2a     3    0     1(correct answer)

            # the total can be reduced to 0 when the total = target and the inner loop is entered.
            # the left pointer can move past the right briefly.
            # the above two design is likely reason that this algorithm is much simpler than mine.
            # I will never be able to come up with this solution on my own.


            while total >= target:
                # the left pointer seems to be able to move past the right pointer.
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans

