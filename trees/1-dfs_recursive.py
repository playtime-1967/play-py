# Recursive DFS (Inorder, Preorder, Postorder Traversal)
# The function goes deep first (visiting all left nodes before moving right).

from ctypes.wintypes import tagRECT
from TreeNode import TreeNode, treeA


def dfs_pre_order(node: TreeNode) -> TreeNode:
    if not node:
        return

    print(node)
    dfs_pre_order(node.left)
    dfs_pre_order(node.right)


def dfs_in_order(node: TreeNode) -> TreeNode:
    if not node:
        return

    dfs_in_order(node.left)
    print(node)
    dfs_in_order(node.right)


def dfs_post_order(node: TreeNode) -> TreeNode:
    if not node:
        return

    dfs_post_order(node.left)
    dfs_post_order(node.right)
    print(node)


def dfs_search(node: TreeNode, target: int) -> TreeNode:
    if not node:
        return False

    if node.val == target:
        return True

    return dfs_search(node.left, target) or dfs_search(node.right, target)


# Call functions
print("-----------dfs_pre_order")
dfs_pre_order(treeA)

print("-----------dfs_in_order")
dfs_in_order(treeA)

print("-----------dfs_post_order")
dfs_post_order(treeA)

print("-----------dfs_search")

find = dfs_search(treeA, 10)
assert find == True
print("find: ", find)
