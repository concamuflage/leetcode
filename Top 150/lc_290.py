class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_array = list(pattern)
        s_array = s.split(" ")
        if len(pattern_array) != len(s_array):
            return False
        dictionary_pattern ={}
        dictionary_s ={}
        for char,word in zip(pattern_array,s_array):
            result_s = dictionary_pattern.get(char)
            if result_s is not None and result_s != word:
                return False
            result_t = dictionary_s.get(word)
            if result_t is not None and result_t != char:
                return False
            dictionary_pattern[char] = word
            dictionary_s[word] = char
        return True
            
        
        
