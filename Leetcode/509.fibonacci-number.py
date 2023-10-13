#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <2:
            return 0 if n == 0 else 1
        m = self.fib(n-1)+self.fib(n-2)
        return m
# @lc code=end

