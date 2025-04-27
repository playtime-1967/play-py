
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path
# equals targetSum.
# A leaf is a node with no children.
from TreeNode import TreeNode, treeA


class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        def hasSum(node: TreeNode, sum: int) -> bool:
            if not node:
                return False

            sum += node.val

            if not node.left and not node.right:
                return targetSum == sum

            return hasSum(node.left, sum) or hasSum(node.right, sum)

        return hasSum(root, 0)

    def hasPathSum_2(self, root: TreeNode, targetSum: int) -> bool:

        if not root and targetSum == 0:
            return False

        stack = [(root, 0)]

        while stack:
            node, sum = stack.pop()

            if node is None:
                continue

            sum += node.val

            if not node.left and not node.right and sum == targetSum:
                return True

            stack.append((node.right, sum))
            stack.append((node.left, sum))

        return False


s = Solution()
result = s.hasPathSum(treeA, 12)
print("hasPathSum: ", result)

result = s.hasPathSum_2(treeA, 12)
print("hasPathSum_2: ", result)
