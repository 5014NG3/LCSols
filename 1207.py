#ez
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        dic = {}
        for n in arr:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        kd = dic.values()

        return len(kd) == len(set(kd))
