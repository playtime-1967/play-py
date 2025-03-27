# remove the nth node from the end of the list and return its head.

from ListNode import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow    
