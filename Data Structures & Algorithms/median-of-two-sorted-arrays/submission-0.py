class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2
        c.sort()
        median = float((c[0] + c[len(c)-1])/2)

        return median