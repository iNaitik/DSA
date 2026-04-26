class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2
        c.sort()
        mid = (0 + len(c)-1)//2
        if len(c)%2 == 0:
            median = (c[mid] + c[mid+1])/2
            return median
        else:
            median = c[mid]
            return median

        