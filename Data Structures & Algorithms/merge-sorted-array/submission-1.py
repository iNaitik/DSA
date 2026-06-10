class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        ans = nums1[:m]   # actual copy of valid elements

        l = 0
        r = 0
        i = 0

        while l < m and r < n:

            if ans[l] <= nums2[r]:
                nums1[i] = ans[l]
                l += 1
            else:
                nums1[i] = nums2[r]
                r += 1

            i += 1

        while l < m:
            nums1[i] = ans[l]
            l += 1
            i += 1

        while r < n:
            nums1[i] = nums2[r]
            r += 1
            i += 1