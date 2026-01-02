


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        left = 0
        right = 0
        result = []
        while right < len(nums) -1:
            if nums[right + 1] == nums[right]+1 or nums[right + 1] == nums[right]:
                right +=1
            else:
                if nums[left] == nums[right]:
                    str1 = str(nums[left])
                else:
                    str1 = str(nums[left]) + "->"+str(nums[right])
                result.append(str1)
                right += 1
                left = right

        if nums[left] == nums[right]:
            str2 = str(nums[left])
        else:
            str2 = str(nums[left]) + "->" + str(nums[right])
        result.append(str2)
        return result


sol = Solution()
print(sol.summaryRanges([])) #[]
print(sol.summaryRanges([1])) #["1"]
print(sol.summaryRanges([1,2,3,6,6,7,7])) #["1 ->3","6","7"]
print(sol.summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
print(sol.summaryRanges([0,2,3,4,6,8,9])) # ["0","2->4","6","8->9"]
        