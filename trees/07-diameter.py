
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

from TreeNode import TreeNode, treeA


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_diameter = [0]

        def heightAndDiameter(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = heightAndDiameter(node.left)
            right_height = heightAndDiameter(node.right)

            diameter = left_height + right_height
            max_diameter[0] = max(max_diameter[0], diameter)

            return 1 + max(left_height, right_height)

        heightAndDiameter(root)
        return max_diameter[0]

    def diameterOfBinaryTree_2(self, root: TreeNode) -> int:

        max_diameter = 0
        heights = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                left_height = heights[node.left] if node.left else 0
                right_height = heights[node.right] if node.right else 0

                diameter = left_height + right_height
                max_diameter = max(max_diameter, diameter)

                heights[node] = 1+max(left_height, right_height)

        return max_diameter


s = Solution()
result = s.diameterOfBinaryTree(treeA)
print("diameterOfBinaryTree: ", result)

result = s.diameterOfBinaryTree_2(treeA)
print("diameterOfBinaryTree_2: ", result)
