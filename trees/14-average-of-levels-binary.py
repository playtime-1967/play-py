
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. .

from TreeNode import TreeNode, treeA
from collections import deque


class Solution:

    def averageOfLevels(self, root: TreeNode) -> any:
        if not root:
            return []

        averages = []
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            sum = 0
            for _ in range(n):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            average = sum / n
            averages.append(average)

        return averages


s = Solution()
result = s.averageOfLevels(treeA)
print("averageOfLevels: ", result)
