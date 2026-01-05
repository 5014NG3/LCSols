class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sz = len(nums)

        left = [0] * sz
        left[0] = nums[0]

        right = [0] * sz
        right[-1] = nums[-1]

        for i in range(sz):
            if i - 1 >= 0:
                left[i] = nums[i] * left[i-1]
                right[sz-1-i] = nums[sz-1-i] * right[sz-i]

        for i in range(sz):
            nnum = 1
            if i - 1 >= 0:
                nnum *= left[i-1]
            if i + 1 < sz:
                nnum *= right[i+1]

            nums[i] = nnum

        return nums

        
