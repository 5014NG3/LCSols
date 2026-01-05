class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # hacker mode, wonder if they actually let people do shit like this in interview

        word_list = s.split()
        word_list.reverse()
        return " ".join(word_list)
