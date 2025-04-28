
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path
# equals targetSum.
# A leaf is a node with no children.
from TreeNode import TreeNode, treeA
from collections import deque


class Solution:

    def levelOrder(self, root: TreeNode) -> any:
        if not root:
            return []

        levels = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return levels


s = Solution()
result = s.levelOrder(treeA)
print("levelOrder: ", result)
