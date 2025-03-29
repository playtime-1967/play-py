# three types of Recursion in DFS; pre-order, in-order, and post-order.
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
    
def dfs_pre_order_2(node: TreeNode) -> TreeNode:
    if not node:
        return

    stack = []
    stack.append(node)

    while stack:
        stack.pop()
        print(node)
        dfs_pre_order(node.left)
        dfs_pre_order(node.right)

    return node


# print(treeA)
print("-----------dfs_pre_order")
dfs_pre_order(treeA)
print("-----------dfs_in_order")
dfs_in_order(treeA)
print("-----------dfs_post_order")
dfs_post_order(treeA)
