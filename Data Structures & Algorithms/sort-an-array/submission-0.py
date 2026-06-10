class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):

            n = len(nums)
            if n == 1:
                return nums
            
            m = len(nums)//2
            L = nums[:m]
            R = nums[m:]

            L = merge_sort(L)
            R = merge_sort(R)

            L_len = len(L)
            R_len = len(R)

            l,r = 0,0
            i = 0
            sort_arr = [0]*n

            while l < L_len and r < R_len:
                if L[l] < R[r]:
                    sort_arr[i] = L[l]
                    l += 1
                else:
                    sort_arr[i] = R[r]
                    r += 1
                i += 1

            while l < L_len:
                sort_arr[i] = L[l]
                i += 1
                l += 1
            
            while r < R_len:
                sort_arr[i] = R[r]
                i += 1
                r += 1
            return sort_arr
        ans = merge_sort(nums)
        return ans





