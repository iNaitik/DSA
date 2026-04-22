class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        output = []

        for i in range(len(nums)):
            l = 0
            r = len(nums)-1
            while l<r:
                if i == l:
                    break
                elif r == i:
                    break
                else:
                    if nums[l]+nums[r]+nums[i] >0:
                        r -= 1
                    elif nums[l]+nums[r]+nums[i] < 0:
                        l += 1
                    elif nums[l]+nums[r]+nums[i] == 0:
                        t = [nums[l],nums[i],nums[r]]
                        if t not in output:
                            output.append(t)
                        l += 1
                        r -= 1
        return output
