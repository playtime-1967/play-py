# Iterative DFS (Using a Stack) instead of recursion

from TreeNode import TreeNode, treeA


def dfs_iterative(node: TreeNode):
    stack = [node]

    while stack:
        node = stack.pop()
        print(node)

        # we first add the right node to the stack, and then the left node; since Stack process the node left at first.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def dfs_search(node: TreeNode, target: int) -> bool:
    if not node:
        return False

    stack = [node]
    while stack:
        node = stack.pop()

        if node.val == target:
            return True

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return False


# The result would be the same as dfs_pre_order(recusrion)
print("-----------dfs_iterative")
dfs_iterative(treeA)


print("-----------dfs_search")
find = dfs_search(treeA, 2)
assert find == True
print("find : ", find)
