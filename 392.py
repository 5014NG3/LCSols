class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        other_i = 0
        cnt = 0

        for sub_c in s:
            while other_i < len(t):
                if sub_c == t[other_i]:
                    cnt += 1
                    other_i += 1
                    break
                other_i += 1
                    

        return cnt == len(s)


        
