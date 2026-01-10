#same as 1004, with k = 1

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        r = 0
        max_sub = 0
        zero_cnt = 0
        while r < len(nums):
            if nums[r] == 0:
                zero_cnt += 1
            
            while zero_cnt > 1:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1

            max_sub = max(max_sub, r-l+1)
            r += 1

        return max_sub - 1
