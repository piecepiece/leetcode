#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        l = 0
        r = len(nums) -1
        while l < r:
            while(l<r and nums[l]!= val):
                l += 1
            while(l<r and nums[r]== val):
                r -=1
            ##元素对换
            nums[l],nums[r] = nums[r],nums[l]
        return l if nums[l] == val else l+1
# @lc code=end

