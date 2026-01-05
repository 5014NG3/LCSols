class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        res = [False] * len(candies)
        max_val = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_val:
                res[i] = True


        return res 

