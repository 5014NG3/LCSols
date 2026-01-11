#yep
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        one_nums = set()
        two_nums = set()

        for n in nums1:
            if n not in nums2:
                one_nums.add(n)

        for n in nums2:
            if n not in nums1:
                two_nums.add(n)

        return [list(one_nums),list(two_nums)]


        
