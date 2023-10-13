#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            ## expand(s,i,i)是 aba 格式， expand(s,i,i+1)是 abba 格式的处理
            ans = max(ans,self.expand(s,i,i),self.expand(s,i,i+1),key=len)
        return ans
    
    def expand(self,s,i,j):
        while i >=0 and j<len(s) and s[i] == s[j]:
            i-=1
            j+=1
        return s[i+1:j]
# @lc code=end

