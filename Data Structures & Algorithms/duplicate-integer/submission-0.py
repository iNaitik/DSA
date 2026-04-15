class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storemap = {}
        f = 0
        for i in nums:
            if i in storemap:
                storemap[i] += 1
                f = 1
            else:
                storemap[i] = 1
        if f == 1:
            return True
        else:
            return False
