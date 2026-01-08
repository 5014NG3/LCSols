#took me a few tries to get this
#its pretty simple after thinking about it in a greedy way

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        max_val = float("-inf")

        while left < right:
            max_val = max(max_val, (right-left) * min(height[left],height[right]) )

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_val
