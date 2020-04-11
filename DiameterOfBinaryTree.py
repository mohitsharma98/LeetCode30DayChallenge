"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, node):
        if node ==None:
            return 0
        return 1 + max(self.height(node.right), self.height(node.left))

    def diameterOfBinaryTree(self, root):

        if root == None:
            return 0
        else:
            lheight = self.height(root.left)
            rheight = self.height(root.right)
            ldepth = self.diameterOfBinaryTree(root.left)
            rdepth = self.diameterOfBinaryTree(root.right)
            
            return max(lheight + rheight, max(ldepth , rdepth))