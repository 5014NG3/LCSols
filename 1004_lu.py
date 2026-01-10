#had to look up solution  on youtube for this one, was stuck
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #find longest window with k <= k zeros
        zero_cnt = 0
        l = 0
        r = 0
        max_sub = 0
        while r < len(nums):
            if nums[r] == 0:
                zero_cnt += 1

            while zero_cnt > k:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            max_sub = max(max_sub, r-l + 1)
            r+=1

        return max_sub

                
