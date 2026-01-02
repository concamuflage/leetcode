from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            key = "".join(sorted(str))
            if key in dict:
                dict[key].append(str)
            else:
                dict[key] = [str]
        return list(dict.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for str in strs:
            bitmap = [0]*26
            for character in str:
                order = ord(character) - ord("a")
                bitmap[order] += 1
            key = tuple(bitmap)
            dict[key].append(str)
        return list(dict.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            bitmap = [0]*26
            for character in str:
                order = ord(character) - ord("a")
                bitmap[order] += 1
            key = tuple(bitmap)
            if key in dict:
                dict[key].append(str)
            else:
                dict[key] = [str]
        return list(dict.values())



sol = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]

strs2 = [""]
print(sol.groupAnagrams(strs2)) #[[""]]

str3 = ["a"]
print(sol.groupAnagrams(str3)) # [["a"]]

str4 = ["ddddddddddg","dgggggggggg"]
print(sol.groupAnagrams(str4))