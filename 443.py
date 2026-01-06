#string compression, struggled a bit on this one
#again don't know what i'm supposed to do in a fucking interview
#can't one shot these problems, unless i have them memorized

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        inline_i = 0

        while i < len(chars):
            start = chars[i]
            i += 1
            cnt = 1
            while i < len(chars) and chars[i] == start:
                i += 1
                cnt += 1

            chars[inline_i] = start
            inline_i += 1
            str_cnt = str(cnt)  


            if cnt > 1 and cnt < 10:
                chars[inline_i] = str_cnt
                inline_i += 1

            if cnt >= 10:
                for xx in list(str_cnt):
                    chars[inline_i] = xx
                    inline_i += 1



        return inline_i



        
