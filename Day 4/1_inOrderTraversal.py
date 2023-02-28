# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
In inorder we go lefr root and right, store it in the result and return it
"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def inOrderHelper(root):

            # Base case if root is none
            if root is None:
                return

            # Traverse left subtree
            inOrderHelper(root.left)

            # Add the value to the result
            result.append(root.val)

            # Traverse right subtree
            inOrderHelper(root.right)

        inOrderHelper(root)
        return result
