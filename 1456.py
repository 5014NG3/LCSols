#same as 643.py
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = "aeiou"
        cnt = 0
        for i in range(k):
            cnt += s[i] in vowels
        
        end = k
        max_vowel = cnt
        while end < len(s):
            cnt += (s[end] in vowels) - (s[end-k] in vowels)
            max_vowel = max(max_vowel, cnt)
            end += 1

        return max_vowel

