class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # create the sliding window
        left_pointer = 0 
        right_pointer = left_pointer + len(needle) - 1

        while right_pointer <= len(haystack):
            # slice 
            str_slice = haystack[left_pointer:right_pointer+1]
            if str_slice == needle:
                return left_pointer
            else: 
                left_pointer += 1
                right_pointer += 1
        return -1

