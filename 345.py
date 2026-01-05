class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        #smart solution is to use while loop, left and right index, and swap like that, go left until hit vowel and go right until hit vowel
        vowels = "AEIOUaeiou"
        lvs = []

        for l in s:
            if l in vowels:
                lvs.append(l)
        res =  ""

        for i in range(len(s)):
            if s[i] in vowels:
                res += lvs.pop()
            else:
                res += s[i]

        return res
