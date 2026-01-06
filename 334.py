class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #ugly inefficient, but i got it
        #the fast solution  is this

        for x in nums:
            if x <= first:
                first = x
            elif x <= second:
                second = x
            else:
                # Found x > second > first
                return True
        return False
      
        if len(nums) < 3:
            return False
        
        max_right = [0] * len(nums)
        max_left = [0] * len(nums)
        r_max = float('inf')
        l_max = float('-inf')
        
        for i in range(len(nums)):
            l_max = max(nums[-1-i],l_max)
            r_max = min(nums[i], r_max)
            max_right[i] = r_max
            max_left[-1-i] = l_max

        for i in range(1, len(nums)):
            if i-1 >= 0 and i+1 < len(nums):
                if nums[i] < max_left[i+1] and nums[i] > max_right[i-1]:
                    return True
    
        return False
