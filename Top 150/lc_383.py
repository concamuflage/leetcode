class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = {}
        for character in magazine:
            frequency[character] = frequency.get(character,0) + 1
        
        for character_2 in ransomNote:
            count = frequency.get(character_2,0)
            if count == 0:
                return False
            else:
                frequency[character_2]-=1

        return True
