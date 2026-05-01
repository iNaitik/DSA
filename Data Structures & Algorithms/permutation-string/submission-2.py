class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False

        freq = [0]*26
        window_freq = [0]*26

        for i in range(len(s1)):
            freq[ord(s1[i])-ord('a')] += 1

        window_size = len(s1)

        for i in range(window_size):
            window_freq[ord(s2[i])-ord('a')] += 1
        
        if freq == window_freq:
            return True

        for i in range(window_size,len(s2)):

            window_freq[ord(s2[i]) - ord('a')] += 1

            window_freq[ord(s2[i - window_size]) - ord('a')] -= 1

            if freq == window_freq:
                return True
        return False




