#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        count = 0
        result = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                result = max(result,count)
                count = 0
        return max(result,count)

# @lc code=end

