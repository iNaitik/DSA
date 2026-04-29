class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        window = set()
        if s == " " or s == "":
            return len(s)
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r += 1
                win_len = len(window)
                ans = max(win_len,ans)
            else:
                win_len = len(window)
                ans = max(win_len,ans)
                window.remove(s[l])
                l += 1
        return ans
