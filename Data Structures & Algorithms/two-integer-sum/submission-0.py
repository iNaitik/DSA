class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hashmap = []
        for i in range(len(nums)):
            # Removed the < target check as numbers can be negative
            Hashmap.append(nums[i])
        for i in range(len(Hashmap)):
            for j in range(len(Hashmap)):
                if i == j:
                    continue
                elif Hashmap[i] + Hashmap[j] == target:
                    return [i,j]