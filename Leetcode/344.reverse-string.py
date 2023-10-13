#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s is None or len(s) == 0:
            return
        self.recursion(s,0,len(s)-1)

    def recursion(self,s,left,right):
        if left>right:
            return
        self.recursion(s,left+1,right-1)
        ## temp = s[left]
        ## s[left] = s[right]
        ## s[right] = temp
        s[left],s[right] = s[right],s[left]

# @lc code=end

