
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from TreeNode import TreeNode, treeA, treeB


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True

        def symmetric(l_node:  TreeNode, r_node: TreeNode) -> bool:
            if not l_node and not r_node:
                return True

            if not l_node or not r_node:
                return False

            if l_node.val != r_node.val:
                return False

            return symmetric(l_node.left, r_node.right) and symmetric(l_node.right, r_node.left)

        return symmetric(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]

        while stack:
            l_node, r_node = stack.pop()

            if not l_node and not r_node:
                continue

            if not l_node or not r_node:
                return False

            if l_node.val != r_node.val:
                return False

            stack.append((l_node.left, r_node.right))
            stack.append((l_node.right, r_node.left))

        return True


s = Solution()
result = s.isSymmetric(treeA)
print("isSymmetric: ", result)
result = s.isSymmetric(treeA)
print("isSymmetric_2: ", result)
