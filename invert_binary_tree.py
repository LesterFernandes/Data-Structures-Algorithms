# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(root):
    def inv(node):
        if node:
            tmp = node.left
            node.left = node.right
            inv(node.left)
            inv(node.right)

    inv(root)
    return root
