class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        Output = []
        product = 1
        product2 = 1
        for i in range(0,len(nums)):
            product = product*nums[i]
            prefix[i] = product
        for i in range(len(nums)-1,-1,-1):
            product2 = product2 * nums[i]
            suffix[i] = product2

        for i in range(len(nums)):
            if i == 0:
                Output.append(suffix[1])
            elif i == (len(nums)-1):
                Output.append(prefix[i-1])
            else:
                k = prefix[i-1]*suffix[i+1]
                Output.append(k)
        return Output
