# Find if there's a cycle in nodes of a linked list.
from ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

    def hasCycle_2(self, head) -> bool:

        set = []

        while head:
            if head in set:
                return True

            set.append(head)
            head = head.next

        return False
