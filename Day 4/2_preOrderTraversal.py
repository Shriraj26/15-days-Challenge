# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Here we go as root, left, right
"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def preOrderHelper(root):

            if not (root):
                return

            # Add the root to result
            result.append(root.val)

            # go left
            preOrderHelper(root.left)

            # go right
            preOrderHelper(root.right)

        preOrderHelper(root)
        return result
