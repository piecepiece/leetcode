#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ## 因为是正反的，所以只有31bit可以存储数据
        MAX_INT = 2 ** 31 -1
        MIN_INT = -2 ** 31
        reverse = 0

        while x != 0:
            if (reverse > MAX_INT /10 or reverse < MIN_INT/10):
                return 0
            ## % -10 only apply for python
            digit = x%10 if x >0 else x %-10
            reverse = reverse * 10 + digit
            ## 不能用floor这里因为负数要向上取整
            x = math.trunc(x/10)
        return reverse
# @lc code=end

