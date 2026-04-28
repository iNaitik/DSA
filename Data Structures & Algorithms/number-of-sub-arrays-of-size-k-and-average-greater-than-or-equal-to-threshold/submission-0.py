class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        store = 0
        count = 0

        for i in range(len(arr)):
            store += arr[i]
            if i >= k:
                store -= arr[i-k]
            if i >= k-1:
                avg = store/k
                if avg >= threshold:
                    count += 1            
        return count