# DFS using loop and stack instead of Recursion.
from TreeNode import TreeNode, treeA


def dfs_loop(node: TreeNode) -> TreeNode:
    stack = [node]

    while stack:
        node = stack.pop()
        print(node)

        # we first add the right node to the stack, and then the left node; since Stack process the node left at first.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# print(treeA)
# the result would be the same as dfs_pre_order(recusrion)
print("-----------dfs_loop")
dfs_loop(treeA)
