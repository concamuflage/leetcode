class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for array_index,num in enumerate(nums):
            found_index = seen.get(num)
            if found_index is not None:
                distance = array_index - found_index
                if distance <= k:
                    return True
            seen[num] = array_index

        return False
