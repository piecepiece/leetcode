#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if s is None or len(s) == 0 or len(s) <k:
            return 0
        hashset = set(['a','e','i','o','u'])
        res,count = 0,0
        for i in range(0,k):
            if s[i] in hashset:
                count = count +1
        res = max (res,count)

        for i in range(k,len(s)):
            out = s[i-k]
            inc = s[i]
            if out in hashset:
                count = count-1
            if inc in hashset:
                count = count+1
            res = max(res,count)
        return res

# @lc code=end

