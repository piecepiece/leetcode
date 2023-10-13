#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        mapping = {}
        res = 0
        while j < len(s):
            if s[j] not in mapping or i>mapping[s[j]]:
                res = max(res,(j-i+1))
                mapping[s[j]] = j
            else:
                ## 存在重复，所以移动i/左边的指针，直到重复消失
                i = mapping[s[j]]+1
                res = max(res,j-i+1)
                j -=1
            j+=1
        return res

# @lc code=end

