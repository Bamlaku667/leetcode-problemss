class ListNode():
     def __init__(self, val = 0, next = None):
          self.val = val
          self.next = next
def removeNthFromEnd(head, n):
        
        #using two pointer approach for solving in one pass
        dummy = ListNode(0, head)
        slow = dummy 
        fast = dummy
        for _ in range(n+1):
            fast = fast.next

        # now we have n gap between fast and slow

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next