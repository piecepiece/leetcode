#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap,num*(-1))
        while k>1:
            heapq.heappop(heap)
            k=k-1
        return heapq.heappop(heap)*(-1)
# @lc code=end

