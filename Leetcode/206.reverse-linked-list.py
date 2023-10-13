#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        while head is not None and head.next is not None:
            dnext = dummy.next
            hnext = head.next
            dummy.next = hnext
            head.next = hnext.next
            hnext.next = dnext
        return dummy.next
# @lc code=end

