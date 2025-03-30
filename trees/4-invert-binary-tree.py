# Given the root of a binary tree, invert the tree, and return its root.

from TreeNode import TreeNode, treeA, print_tree


class Solution:
    # recusrison
    def invertTree(self, node: TreeNode) -> TreeNode:
        if not node:
            return None

        # Swap left and right
        node.left, node.right = node.right, node.left
        self.invertTree(node.left)
        self.invertTree(node.right)
        return node

    # iterative
    def invertTree_2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            # Swap left and right
            node.left, node.right = node.right, node.left

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return root


print("-----------before inverting")
treeA
print_tree(treeA)
print("\n-----------after")
inverted = Solution().invertTree(treeA)
print_tree(inverted)