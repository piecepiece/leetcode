#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend >= 0 and divisor < 0 or dividend <0 and divisor >=0:
            sign = -1
        else:
            sign = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = len(range(0,dividend - divisor+1, divisor))

        if sign == -1:
            result = result * (-1)

        MIN_LIMIT = -2**31
        MAX_LIMIT = 2**31-1

        result = min(max(result,MIN_LIMIT),MAX_LIMIT)

        return result

# @lc code=end

