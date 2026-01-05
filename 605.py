class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        
        bed_size = len(flowerbed)
        i_greed_place = 0
        max_n = 0



        for i in range(bed_size):
            if flowerbed[i] == 0: 
                #chat gpt optimize , added or i == bed_size -1 , same as it being empty
                a = i + 1 < bed_size and flowerbed[i+1] == 0 or i == bed_size - 1
                b = i-1 != i_greed_place and i - 1 > 0 and flowerbed[i-1] == 0 or i == 0

                if a and b:
                    i_greed_place = i
                    max_n += 1




        return max_n >= n





