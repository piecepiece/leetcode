#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if people is None or len(people) == 0:
            return 0
        people.sort()
        i,res = 0,0
        j = len(people) -1
        while(i<=j):
            if people[i] + people[j]<=limit:
                i=i+1
            j=j-1
            res=res+1
        return res
# @lc code=end

