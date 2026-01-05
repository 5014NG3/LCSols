class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1[0] != str2[0]:
            return ""

        min_len = min(len(str1), len(str2))
        max_sub_len = 0
        
        for i in range(min_len):
            prefix = str1[:i+1]

            a = str1.split(prefix)
            b = str2.split(prefix)

            if "".join(a) == "" and "".join(b)  == "":
                max_sub_len = len(prefix)


        return str1[:max_sub_len]
         
