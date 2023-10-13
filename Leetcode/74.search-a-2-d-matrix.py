#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) ==0:
            return False
        row = len(matrix)
        ##第0行matrix的长度
        col = len(matrix[0])
        l = 0
        r = row*col -1
        while l<=r:
            m = l+ (r-l)//2
            ## m//col得到x， m%col得到y
            element = matrix[m//col][m%col]
            if element == target:
                return True
            elif element > target:
                r = m-1
            else:
                l = m+1
        return False
            
# @lc code=end

