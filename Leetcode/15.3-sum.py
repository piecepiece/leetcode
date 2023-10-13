#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## 排序
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            ## 在这里检查了 i的值是不是重复的
            ## continue 会直接跳过下面的code
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total <0:
                    l+=1
                elif total > 0:
                    r -=1
                else: 
                    triplet = [nums[i],nums[l],nums[r]]
                    ans.append(triplet)
                    while l < r and nums[l] == triplet[1]:
                        l +=1
                    while l < r and nums[r] == triplet[2]:
                        r -=1
        return ans
# @lc code=end

