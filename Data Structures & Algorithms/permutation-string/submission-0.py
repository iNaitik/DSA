class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        window_freq = [0] * 26

        # build freq for s1
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1

        win_size = len(s1)

        # build first window
        for i in range(win_size):
            window_freq[ord(s2[i]) - ord('a')] += 1

        if freq == window_freq:
            return True

        # slide window
        for i in range(win_size, len(s2)):
            # add new char
            window_freq[ord(s2[i]) - ord('a')] += 1
            
            # remove old char
            window_freq[ord(s2[i - win_size]) - ord('a')] -= 1

            if freq == window_freq:
                return True

        return False