class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        prev_smaller = [-1] * n
        next_smaller = [n] * n

        # Previous Smaller
        for i in range(n):
            if stack and heights[i] > heights[stack[-1]]:
                prev_smaller[i] = stack[-1]
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()

                if stack:
                    prev_smaller[i] = stack[-1]

                stack.append(i)

        stack = []

        # Next Smaller
        for i in range(n - 1, -1, -1):
            if stack and heights[i] > heights[stack[-1]]:
                next_smaller[i] = stack[-1]
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()

                if stack:
                    next_smaller[i] = stack[-1]

                stack.append(i)

        max_area = 0

        for i in range(n):
            w = next_smaller[i] - prev_smaller[i] - 1
            area = heights[i] * w
            max_area = max(max_area, area)

        return max_area