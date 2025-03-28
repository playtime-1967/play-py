from ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev  
    
    # recursive
    def reverseList_2(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        newHead = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None

        return newHead
