class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        [1,2,3,4]
        dic[k-num] += 1
        """
        dic = {}

        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        res = 0

        for n in nums:
            if k-n in dic and dic[k-n] > 0:
                dic[k-n] -= 1
                res += 1


        return res // 2


        
