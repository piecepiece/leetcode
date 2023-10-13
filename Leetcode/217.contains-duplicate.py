#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        hashTable = {}
        for num in nums:
            if num not in hashTable:
                hashTable[num]=1
            else:
                hashTable[num]=hashTable.get(num) + 1
        for v in hashTable.values():
            if v>1:
                return True
        return False


# @lc code=end

