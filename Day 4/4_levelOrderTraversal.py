"""
1. Add root to queue
2. loop till q is not empty,
3. add empty arr to the result
4. loop till len of elems in q is 

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        # This is how u add elem to deque in Python
        q = deque([root])

        level = 0
        result = []

        while len(q) > 0:

            result.append([])
            counter = len(q)
            while counter > 0:

                curr = q.popleft()
                result[level].append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

                counter -= 1

            level += 1

        return result
