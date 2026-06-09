class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0, 0]

        # Count frequencies
        for i in range(len(nums)):
            counts[nums[i]] += 1

        # Rebuild array
        i = 0

        for n in range(len(counts)):

            for j in range(counts[n]):

                nums[i] = n
                i += 1
