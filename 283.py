#had trouble with this one,
#don't really understand why adding 
# if cnt != i, fixed the issue, but it did for some reason
# anyway spent way longer thatn i wanted on this


#my logic makes sense, track position of where to insert non zero values
#when non zero value is found insert at count position, then increase it
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if cnt != i:
                    nums[cnt] = nums[i]
                    nums[i] = 0
                cnt += 1
    
