class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

# Helper function to print a Tree

def print_tree(tree: TreeNode):
    if not tree:
        return

    while tree:
        print(tree.val, end=" -> ")
        return print_tree(tree.left) or print_tree(tree.right)


# sample data
treeA = TreeNode(1)
treeB = TreeNode(2)
treeC = TreeNode(3)
treeD = TreeNode(4)
treeE = TreeNode(5)
treeF = TreeNode(10)

treeA.left = treeB
treeA.right = treeC
treeB.left = treeD
treeB.right = treeE
treeC.left = treeF

# It only prints 1 -So we need to use dfs/bfs to traverse all nodes.
# print("----------without traverse")
# print(treeA)
# print_tree(treeA)
