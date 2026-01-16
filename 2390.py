#can be done with for loop only 

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stck = []
        i = 0
        while i < len(s):
            stck.append(s[i])
            i+= 1

            while i < len(s) and s[i] == "*":
                stck.pop()
                i += 1

        return "".join(stck) 
                
        

