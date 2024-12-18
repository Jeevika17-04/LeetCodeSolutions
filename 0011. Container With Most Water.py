class Solution(object):
    def maxArea(self, height):
        max_area = 0
        n = len(height)
        i, j = 0, n - 1
        while i < j:
            if height[i] < height[j]:
                if max_area < height[i] * (j - i):
                    max_area = height[i] * (j - i)
                i += 1
            else:
                if max_area < height[j] * (j - i):
                    max_area = height[j] * (j - i)
                j -= 1
        return max_area
