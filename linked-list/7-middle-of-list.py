# Find middle of a list node

from ListNode import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow    
