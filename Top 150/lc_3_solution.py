class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}          # char -> most recent index
        left = 0
        best = 0

        for right, number in enumerate(s):
            if number in last and last[number] >= left:
                left = last[number] + 1
            last[number] = right
            best = max(best,right - left + 1)
        return best

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
