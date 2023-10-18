# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head ):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0, head)
        prev = dummy 
        # d  -->  1  -->  2 --> 3--> 4 --> null
        # prev      
        while head and head.next:
            
            first_node = head
            second_node = first_node.next

            # d  -->  1  -->  2 --> 3--> 4 --> null
            # prev    f       s

            #swapping 

            # d  -->  2  -->  1 --> 3--> 4 --> null
            # prev            f      
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            

            #for next iteration modify the head
            head = first_node.next
            prev = first_node

            # d  -->  1  -->  2 --> 3-->  4 --> null
            #               prev    head
        return dummy.next
        
        