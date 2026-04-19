class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stk and height < stk[-1][0]:
                h, j = stk.pop()
                w = i - j
                max_area = max(max_area, h * w)
                start = j

            stk.append((height, start))

        while stk:
            h, j = stk.pop()
            w = n - j
            max_area = max(max_area, h * w)

        return max_area