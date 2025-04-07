# three types of Recursion in DFS; pre-order, in-order, and post-order.
from requests import head
from TreeNode import TreeNode, treeA
from collections import deque


def bfs_level_order(node: TreeNode):

    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        print(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def bfs_search(node: TreeNode, target: int) -> bool:

    if not head:
        return False

    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()

        if node.val == target:
            return True

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


print("-----------bfs_level_order")
bfs_level_order(treeA)


print("-----------bfs_search")
find = bfs_search(treeA, 2)
assert find == True
print("find : ", find)
