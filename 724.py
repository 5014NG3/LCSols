#shoutout needcode
#spent way too long on dis shit
#was trying to use while loops, and 
#attacking this from left and right, sum left, then right, its was fucked

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i

            left_sum += nums[i]


        return -1
            

