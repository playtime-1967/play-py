
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

from TreeNode import TreeNode, treeA


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        balanced = [True]

        def height(root: TreeNode) -> int:
            if not root:
                return 0

            left_height = height(root.left)
            if balanced[0] is False:
                return 0

            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]


s = Solution()
result = s.isBalanced(treeA)
print("isBalanced: ", result)
