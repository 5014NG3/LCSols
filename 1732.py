#pinwheel ass question
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        max_gain = 0
        run_sum = 0
        for g in gain:
            run_sum += g
            max_gain = max(max_gain,run_sum)

        return max_gain
        
