class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Hashmap = {}
        ans = []

        for i in range(len(nums)):
            if nums[i] in Hashmap:
                Hashmap[nums[i]] += 1
            else:
                Hashmap[nums[i]] = 1
        
        for key,value in Hashmap.items():
            if value > len(nums)//3:
                ans.append(key)
        return ans