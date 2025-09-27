class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        string_array = s.split(" ")
        lastword = string_array[-1]
        return len(lastword)