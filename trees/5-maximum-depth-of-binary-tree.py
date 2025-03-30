# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from TreeNode import TreeNode, treeA


class Solution:
    # recusrison
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        max_depth = 1 + max(left, right)

        return max_depth

     # iterative
    def maxDepth_2(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth+1))
            if node.left:
                stack.append((node.left, depth+1))

        return max_depth


s = Solution()
mx = s.maxDepth_2(treeA)
print("max_2: ", mx)

max = s.maxDepth(treeA)
print("max: ", max)
