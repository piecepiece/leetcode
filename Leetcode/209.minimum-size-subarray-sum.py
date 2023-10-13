#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums) ==0:
            return 0
        res = len(nums) +1
        total,i,j=0,0,0
        while (j<len(nums)):
            total = total + nums[j]
            j = j+1
            while(total >= target):
                res = min(res,j-i)
                total = total - nums[i]
                i +=1

        return 0 if res == len(nums) + 1 else res
# @lc code=end

