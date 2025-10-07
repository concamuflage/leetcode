# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         compare = {}
#         for index in range(len(s)):
#             value = s[index]
#             key = t[index]
#             result = compare.get(key)
            
#             if  result is None:
#                 # check if any key already has the same value
#                 different_key = [k for k,v in compare.items() if v == value]
#                 if len(different_key) == 0:
#                     compare[key] = value
#                 else:
#                     return False
#             elif result != value:
#                 return False
#         return True
                
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary_s ={}
        dictionary_t ={}
        for char_s,char_t in zip(s,t):
            result_s = dictionary_s.get(char_s)
            if result_s is not None and result_s != char_t:
                return False
            result_t = dictionary_t.get(char_t)
            if result_t is not None and result_t != char_s:
                return False
            dictionary_s[char_s] = char_t
            dictionary_t[char_t] = char_s
        return True

            
        
        
