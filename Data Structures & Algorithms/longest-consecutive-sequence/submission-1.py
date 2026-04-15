class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_a = sorted(nums)
        hashmap = {}
        if not nums:
            return 0
        f = 1
        for i in range(len(sort_a)-1):
            if sort_a[i] in hashmap:
                continue
            elif (sort_a[i+1] - sort_a[i] ==1): 
                f += 1
        return f