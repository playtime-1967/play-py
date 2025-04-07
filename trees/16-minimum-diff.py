
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
from TreeNode import TreeNode, treeA


class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        min_val = [float('inf')]
        prev_val = [None]

        def minimumDiff(node: TreeNode):

            if not node:
                return

            minimumDiff(node.left)

            if prev_val[0] is not None:
                min_val[0] = min(min_val[0], node.val - prev_val[0])

            prev_val[0] = node.val
            minimumDiff(node.right)

        minimumDiff(root)
        return min_val[0]

    def getMinimumDifference_2(self, root: TreeNode) -> int:

        min_val = float('inf')
        stack = []
        prev_val = None
        node = root

        while stack or node:

            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if prev_val is not None:
                min_val = min(min_val, abs(node.val - prev_val))

            prev_val = node.val
            node = node.right
        return min_val


s = Solution()
result = s.getMinimumDifference(treeA)
print("getMinimumDifference: ", result)

result = s.getMinimumDifference_2(treeA)
print("getMinimumDifference_2: ", result)
