
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
from TreeNode import TreeNode, treeA
from collections import deque


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        counter = [k]
        result = [0]

        def smallest(node: TreeNode) -> int:
            if not node:
                return
            smallest(node.left)

            if counter[0] == 1:
                result[0] = node.val

            counter[0] -= 1
            if counter[0] > 0:
                smallest(node.right)

        smallest(root)
        return result[0]

    def kthSmallest_2(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []

        while True:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            node = node.right


s = Solution()
result = s.kthSmallest(treeA, 3)
print("kthSmallest: ", result)

result = s.kthSmallest_2(treeA, 3)
print("kthSmallest_2: ", result)
