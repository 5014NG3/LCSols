class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """


        run_sum = 0
        for i in range(k):
            run_sum += nums[i]

        end = k
        max_sum = run_sum
        while end < len(nums):
            run_sum += (nums[end] - nums[end-k])
            max_sum = max(max_sum, run_sum)
            end += 1

        return float(max_sum) / k
