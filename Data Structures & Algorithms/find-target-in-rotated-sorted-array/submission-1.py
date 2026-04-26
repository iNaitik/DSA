class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = 1
        st = 0
        ft = len(nums) - 1

        while nums[r]>nums[l]:
            l += 1
            r += 1
        while st<=l:
            mid = (st + l)//2
            if nums[mid] > target:
                l = mid - 1
            elif nums[mid] < target:
                st = mid + 1
            elif nums[mid] == target:
                return mid
        while r<=ft:
            mid = (r + ft)//2
            if nums[mid] > target:
                ft = mid - 1
            elif nums[mid] < target:
                r = mid + 1
            elif nums[mid] == target:
                return mid
        return -1

        
        
                