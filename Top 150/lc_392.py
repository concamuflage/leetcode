class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0
        while pointer_s < len(s) :
            if pointer_t >= len(t):
                return False
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1                
            pointer_t += 1
        return True
