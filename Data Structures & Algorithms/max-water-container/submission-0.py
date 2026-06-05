class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max = 0

        for i in range(1, len(heights)):

            for j in range(i):

                val = min(heights[i], heights[j]) * (i - j)
                
                if val > max:

                    max = val

        return max