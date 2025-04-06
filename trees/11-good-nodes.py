
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
from TreeNode import TreeNode, treeA


class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0
        stack = [(root, float('-inf'))]

        while stack:
            node, max_value = stack.pop()

            if node.val >= max_value:
                good_nodes += 1
                max_value = node.val

            if node.right:
                stack.append((node.right, max_value))

            if node.left:
                stack.append((node.left, max_value))

        return good_nodes


s = Solution()
result = s.goodNodes(treeA)
print("goodNodes: ", result)
