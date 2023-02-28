# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Left right root
"""


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postOrderHelper(root):
            if not (root):
                return

            # Go Left
            postOrderHelper(root.left)

            # Go Right
            postOrderHelper(root.right)

            # Append to the result
            result.append(root.val)

        postOrderHelper(root)
        return result
