
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and
# false otherwise.

from TreeNode import TreeNode, treeA


class Solution:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def sameTree(q:  TreeNode, p: TreeNode) -> bool:
            if not q and not p:
                return True

            if not q or not p:
                return False

            if q.val != p.val:
                return False

            return sameTree(q.left, p.left) and sameTree(q.right, p.right)

        def hasSubtree(root: TreeNode) -> bool:

            if not root:
                return False

            if sameTree(root, subRoot):
                return True

            return hasSubtree(root.left) or hasSubtree(root.right)

        return hasSubtree(root)

    def isSubtree_2(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def sameTree_dfs(tree:  TreeNode, subtree: TreeNode) -> bool:
            stack = [(tree, subtree)]

            while stack:
                tree, subtree = stack.pop()

                if not tree and not subtree:
                    continue

                if not tree or not subtree:
                    return False

                if tree.val != subtree.val:
                    return False

                stack.append((tree.left, subtree.left))
                stack.append((tree.right, subtree.right))

            return True

        def hasSubtree(root: TreeNode) -> bool:
            if root is None:
                return False

            if sameTree_dfs(root, subRoot):
                return True

            return hasSubtree(root.left) or hasSubtree(root.right)

        return hasSubtree(root)


s = Solution()
result = s.isSubtree(treeA, treeA)
print("isSubtree: ", result)

result = s.isSubtree_2(treeA, treeA)
print("isSubtree_2: ", result)
