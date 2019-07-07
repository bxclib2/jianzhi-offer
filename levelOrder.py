# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        res.append([root.val])
        level = [root]
        while True:
            level_temp = []
            res_temp = []
            for n in level:
                if n.left is not None:
                    level_temp.append(n.left)
                    res_temp.append(n.left.val)
                if n.right is not None:
                    level_temp.append(n.right)
                    res_temp.append(n.right.val)
            if res_temp!=[]:
                res.append(res_temp)
                level = level_temp
            else:
                break
        return res
