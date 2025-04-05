
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

from math import fabs
from TreeNode import TreeNode, treeA, treeB


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def balance(q:  TreeNode, p: TreeNode) -> bool:
            if not q and not p:
                return True

            if (not q and p) or (not p and q):
                return False

            if q.val != p.val:
                return False

            return balance(q.left, p.left) and balance(q.right, p.right)

        return balance(q, p)

    def isSameTree_2(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(q, p, False)]
        while stack:
            node_p, node_q, visited = stack.pop()

            if not node_p and not node_q:
                continue

            if (not node_p and node_q) or (not node_q and node_p):
                return False

            if node_p.val != node_q.val:
                return False

            if not visited:
                stack.append((node_p, node_q, True))
                stack.append((node_p.left, node_q.left, False))
                stack.append((node_p.right, node_q.right, False))

        return True


s = Solution()
# ------------------- NOT the same
result = s.isSameTree(treeA, treeB)
print("isSameTree: ", result)
result = s.isSameTree_2(treeA, treeB)
print("isSameTree_2: ", result)

# ------------------- the same
result = s.isSameTree(treeA, treeA)
print("isSameTree: ", result)

result = s.isSameTree_2(treeA, treeA)
print("isSameTree_2: ", result)
