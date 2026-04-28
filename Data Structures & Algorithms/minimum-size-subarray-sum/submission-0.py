class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        length = float("inf")
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                length = min(r - l + 1,length)
                total -= nums[l]
                l += 1
        if length == float("inf"):
            return 0
        else:
            return length
