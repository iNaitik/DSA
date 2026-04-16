class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in numset:
                next_num = i + 1
                length = 1
                while next_num in numset:
                    length += 1
                    next_num += 1
                longest = max(length,longest)

        return longest