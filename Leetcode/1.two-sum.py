#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    result.append(i)
                    result.append(j)
                    return result


# @lc code=end

