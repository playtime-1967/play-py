
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from re import L
from TreeNode import TreeNode, treeA, treeB


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        def symmetric(l_node:  TreeNode, r_node: TreeNode) -> bool:
            if not l_node and not r_node:
                return True

            if (not l_node and r_node) or (not r_node and l_node):
                return False

            if l_node.val != r_node.val:
                return False

            return symmetric(l_node.left, r_node.right) and symmetric(l_node.right, r_node.left)

        return symmetric(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right, False)]

        while stack:
            l_node, r_node, visited = stack.pop()

            if not l_node and not r_node:
                continue

            if (not l_node and r_node) or (not r_node and l_node):
                return False

            if l_node.val != r_node.val:
                return False

            if not visited:
                stack.append((l_node, r_node, True))
                stack.append((l_node.left, r_node.right, False))
                stack.append((l_node.right, r_node.left, False))

        return True


s = Solution()
# ------------------- NOT the same
result = s.isSymmetric(treeA)
print("isSymmetric: ", result)
result = s.isSameTree_2(treeA, treeB)
print("isSameTree_2: ", result)
