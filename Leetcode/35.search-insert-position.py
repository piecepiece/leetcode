#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        l= 0
        r=len(nums)
        while(l<r):
            m = l+ (r-l)//2
            if nums[m] == target:
                return m
            elif nums[m] >target:
                r = m
            else:
                l = m+1
        return l
# @lc code=end

