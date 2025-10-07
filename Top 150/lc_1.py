class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = {}
        #
        for index in range(len(nums)):
            number = nums[index]
            index_list = result.get(number)
            if index_list is not None:
                index_list.append(index)
                continue
            result[number] = [index]
        
        for key in result.keys():
            complement = target - key
            result1 = result.get(complement)
            if result1 is not None:
                if complement == key:
                    if len(result1) > 1:
                        return [result1[0],result1[1]]
                    else:
                        continue
                else:
                    return [result[key][0],result[complement][0]]
                