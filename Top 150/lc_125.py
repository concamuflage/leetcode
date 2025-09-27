class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([character for character in s if character.isalnum()])
        cleaned = cleaned.lower()

        if len(cleaned) == 1:
            return True
        left_pointer = 0
        right_pointer = len(cleaned) - 1

        while right_pointer > left_pointer:
            if cleaned[left_pointer] == cleaned[right_pointer]:
                left_pointer +=1
                right_pointer -= 1
            else:
                return False
        
        return True