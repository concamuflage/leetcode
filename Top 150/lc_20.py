class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {
                '(': ')',
                '[': ']',
                '{': '}'
                }

        stack = []
        for index,char in enumerate(list(s)):
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0 :
                    return False
                char_on_top = stack.pop()
                if pairs[char_on_top] != char:
                    return False
        if len(stack) != 0:
            return False
        return True