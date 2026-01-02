class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix_tree = Trie()

        # to construct the prefix tree
        for str in strs:
            prefix_tree.insert(str)

        # count the number of nodes that have no branches.

        count = 0
        node = prefix_tree.root
        while True:
            if node.is_end or len(node.children) !=1:
                break
            count += 1
            node = next(iter(node.children.values()))
        # slice from the first word
        first_word = strs[0]
        # for special cases like "ab" and "a"
        # the count would be 2, so it need correction
        result = first_word[0:count]
        return result

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,str):
        node = self.root
        for ch in str:
            if ch not in  node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True



s = Solution()
print(s.longestCommonPrefix(["abab","aba",""]))





