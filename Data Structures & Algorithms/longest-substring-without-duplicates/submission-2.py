class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        ans = 0

        mp = {}

        left = 0
        for right in range(len(s)):
            window += s[right]
            
            while s[right] in mp:
                left += 1
                cut = window[:1]
                window = window[1:]
                mp.pop(cut, None)
            
            mp[s[right]] = 1
            if len(window) > ans:
                ans = len(window)

        return ans