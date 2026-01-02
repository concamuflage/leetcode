class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        s1 = min(strs)
        s2 = max(strs)

        i = 0
        limit = min(len(s1), len(s2))
        while i < limit and s1[i] == s2[i]:
            i += 1

        return s1[:i]

s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))



