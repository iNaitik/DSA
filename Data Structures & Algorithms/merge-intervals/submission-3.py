class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                Merged_interval = [ans[-1][0],
                max(intervals[i][1],ans[-1][1])]
                ans.pop()
                ans.append(Merged_interval)
            else:
                ans.append(intervals[i])
        return ans