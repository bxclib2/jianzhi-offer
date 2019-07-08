# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        root = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == root:
                break
        left_inorder = inorder[:i]
        if len(left_inorder)<len(inorder)-1:
            right_inorder = inorder[i+1:]
        else:
            right_inorder = []
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        res = TreeNode(root)
        res.left = self.buildTree(left_preorder,left_inorder)    
        res.right = self.buildTree(right_preorder,right_inorder)  
        return res
