# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        l = []
        if root is None:
            return res
        l.append(root)

        while len(l)!=0:
            n = l.pop()
            if n.left is None and n.right is None:
                res.append(n.val)
            else:
                l.append(TreeNode(n.val))
            if n.right is not None:
                l.append(n.right)  
            if n.left is not None:
                l.append(n.left)
        return res
