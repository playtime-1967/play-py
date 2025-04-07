
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from TreeNode import TreeNode, treeA


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(node: TreeNode, minn: int, maxx: int) -> bool:

            if not node:
                return True

            if node.val >= maxx or node.val <= minn:
                return False

            return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)

        return is_valid(root, float('-inf'), float('inf'))

    def isValidBST_2(self, root: TreeNode) -> bool:
        minn = float('-inf')
        maxx = float('inf')
        stack = [(root, minn, maxx)]

        while stack:
            node, minn, maxx = stack.pop()

            if not node:
                continue

            if node.val <= minn or node.val >= maxx:
                return False

            stack.append((node.left, minn, node.val))
            stack.append((node.right, node.val, maxx))

        return True


s = Solution()
result = s.isValidBST(treeA)
print("isValidBST: ", result)

result = s.isValidBST_2(treeA)
print("isValidBST_2: ", result)
