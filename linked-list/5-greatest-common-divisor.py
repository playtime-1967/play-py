# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them. Return the linked list after insertion.

import math
from ListNode import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        ahead = head.next

        while ahead:
            gcd = math.gcd(current.val, ahead.val)
            greatest = ListNode(gcd, ahead)

            current.next = greatest
            current = ahead
            ahead = ahead.next

        return head
