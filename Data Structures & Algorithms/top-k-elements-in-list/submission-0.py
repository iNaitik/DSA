class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hashmap = {}
        for i in nums:
            if i not in Hashmap:
                Hashmap[i] = 1
            else:
                Hashmap[i] += 1
        freq = sorted(Hashmap.items(), key = lambda x: x[1], reverse = True)
        output = []
        for i in range(k):
            output.append(freq[i][0])
        return output