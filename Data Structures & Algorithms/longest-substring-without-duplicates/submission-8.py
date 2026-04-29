class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        window = set()
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r += 1
                ans = max(r - l,ans)
            else:
                window.remove(s[l])
                l += 1
        return ans
