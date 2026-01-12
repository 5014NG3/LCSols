#fun problem

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = {}

        for row in grid:
            tup_row = tuple(row)
            if tup_row not in dic:
                dic[tup_row] = 1
            else:
                dic[tup_row] += 1
        res = 0
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            tup_col = tuple(col)
            if tup_col in dic:
                res += dic[tup_col]


        return res

        
