class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        area = 0
  

        for i , hieght in enumerate(heights):
            start = i
            while stack and stack[-1][0]>hieght:
                h,j = stack.pop()
                w = i - j
                a = h * w
                area = max(area,a)
                start = j
            stack.append((hieght,start))
        
        while stack:
            h,j = stack.pop()
            w = n-j
            a = h*w
            area = max(area,a)
        return area
