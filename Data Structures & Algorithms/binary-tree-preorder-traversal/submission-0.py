# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root):
            curr = root
            if not root:
                return
            res.append(curr.val)
            left = preorder(curr.left)
            right = preorder(curr.right)
        preorder(root)
        return res