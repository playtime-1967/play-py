# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them. Return the linked list after insertion.
import math
from ListNode import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        next = head.next

        while next:
            gcd = math.gcd(current.val, next.val)
            greatest = ListNode(gcd, next)
            current.next = greatest
            current = next
            next = next.next

        return head
