class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            res = nums[l]
            if res <= nums[r]:
                res = nums[l]
                r -= 1
            else:
                l +=1
        return res
