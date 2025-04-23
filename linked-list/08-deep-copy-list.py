# deep copy of every node, its next&random node

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def deepCopyRandomList(self, head: Node) -> Node:

        if not head:
            return None

        current = head
        map = {}

        while current:
            newNode = Node(current.val)
            map[current] = newNode
            current = current.next

        current = head

        while current:
            newNode = map[current]
            newNode.next = map[current.next] if current.next else None
            newNode.random = map[current.random] if current.random else None
            current = current.next

        return map[head]
