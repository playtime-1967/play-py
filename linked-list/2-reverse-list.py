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
