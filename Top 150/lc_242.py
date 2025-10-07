class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_list = [0]*26
        base = ord("a")
        for char in s:
            char_list[ord(char)-base] += 1
        for char in t:
            if char_list[ord(char)-base] == 0:
                return False
            char_list[ord(char)-base] -= 1
        return True