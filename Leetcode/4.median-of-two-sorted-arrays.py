#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ## 先把两个list 合起来，通过sort使顺序排列
        merge = nums1 + nums2
        merge.sort()
        ## 如果 %2 ==1，则是基数，直接return
        if len(merge)%2 == 1:
            return float(merge[len(merge)//2])
        ## 偶数，需要两数相加
        else:
            middle1 = merge[len(merge)//2 -1]
            middle2 = merge[len(merge)//2]
            return float(float(middle1)+float(middle2))/2
# @lc code=end

