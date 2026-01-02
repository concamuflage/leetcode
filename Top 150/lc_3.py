class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        left = 0
        right = 0
        in_window = {}
        in_window[s[left]] = 1
        max_window_size = 1
            # try to expand the sliding window rightward.
        while right <= len(s) -2:
            right += 1
            # window growth failed.
            if s[right] in in_window:
                # remove the leftmost letter from in_window.
                del in_window[s[left]]
                right -=1
                # move current window to the right by 1 position.
                left +=1
                if right < left:
                    right = left
                    in_window[s[left]] = 1

            # window can grow
            else:
                # put the new letter in in-window.
                in_window[s[right]] = 1
                current_window_size = right - left + 1
                max_window_size = max(current_window_size,max_window_size)

        return max_window_size


s = Solution()
print(s.lengthOfLongestSubstring("bbbbb"))  # 0
print(s.lengthOfLongestSubstring("a"))   # 1
print(s.lengthOfLongestSubstring("aa"))  # 1
print(s.lengthOfLongestSubstring("ab"))  # 2
print(s.lengthOfLongestSubstring("abb"))  # 2
print(s.lengthOfLongestSubstring("aaa"))  # 1
print(s.lengthOfLongestSubstring("aba"))  # 2
print(s.lengthOfLongestSubstring("dvdf"))  # 2

