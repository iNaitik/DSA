class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hashmap = {}
        for i ,num in enumerate(nums):
            complement = target - num
            if complement in Hashmap:
                return [Hashmap[complement],i]
            Hashmap[num] = i