#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        temp = x
        while temp != 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10

        return reverse==x
# @lc code=end

