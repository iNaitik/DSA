# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def counts(root,max_val):
            curr = root
            if not curr:
                return
            if curr.val >= max_val:
                max_val = max(max_val,curr.val)
                self.good += 1
            counts(curr.left,max_val)
            counts(curr.right, max_val)
        counts(root,float('-inf'))
        return self.good


