class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        #can be optimized
        #just sort the two strings , and check if they are equal
        #also check if both words have the same characters, a set 
        if len(word1) != len(word2):
            return False

        one_dic = {}
        two_dic = {}

        for i in range(len(word1)):
            if word1[i] in one_dic:
                one_dic[word1[i]] += 1
            else:
                one_dic[word1[i]] = 1

            if word2[i] in two_dic:
                two_dic[word2[i]] += 1
            else:
                two_dic[word2[i]] = 1
        #check all charcters the sma
        if sorted(one_dic.keys()) != sorted(two_dic.keys()):
            return False

        if sorted(one_dic.values()) == sorted(two_dic.values()):
            return True


        return False
        
