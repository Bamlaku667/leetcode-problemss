# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        curr = head.next
        while curr:
            temp = curr.next


            if prev.val > curr.val:
                prev.next = temp
                curr.next = temp
                prev = curr
            curr = curr.next

        