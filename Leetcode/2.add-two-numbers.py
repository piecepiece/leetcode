#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        ## 是否有进位
        next1 = 0
        ## 一个一直指向起点，一个随着计算移动
        dummy = ListNode()
        cur = dummy

        while(l1 != None and l2 != None):
            total = l1.val + l2.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            ## 所有点往后移动
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            total = l1.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l1 = l1.next
        
        while l2 != None:
            total = l2.val + next1
            cur.next = ListNode(total % 10)
            next1 = total // 10
            cur = cur.next
            l2 = l2.next

        ## 完成计算后如果next1还有值
        if next1 != 0:
            cur.next = ListNode(next1)

        return dummy.next
# @lc code=end

