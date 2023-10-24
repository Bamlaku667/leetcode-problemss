# Definition for singly-linked list.
from typing import Optional
 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if head.next:
            mid = self.find_mid(head)
            first_half = head
            second_half = mid.next
            mid.next = None

            first_half = self.sortList(first_half)
            second_half = self.sortList(second_half)

        return self.merge_list(first_half, second_half)


    def merge_list(list1, list2):
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next

            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1: 
            curr.next = list1
        if list2: 
            curr.next = list2

        return dummy.next

    def find_mid(head: ListNode):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        return slow 