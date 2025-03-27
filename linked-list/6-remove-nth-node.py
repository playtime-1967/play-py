# remove the nth node from the end of the list and return its head.

from ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy
        
        for _ in range(n+1):
            ahead=ahead.next
            
        while ahead:
            ahead= ahead.next
            behind=behind.next
            
        behind.next= behind.next.next    

        return dummy.next    
        
