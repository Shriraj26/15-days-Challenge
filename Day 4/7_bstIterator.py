# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Refer Neetcode video for this... We maintain a stack to do the operations
and only append the left pointers in the stack
https://www.youtube.com/watch?v=RXy5RzGF5wo
Just walkthrough an example and you will get a clear picture..
This approach stores atmost h nodes in the stack thus the 
space complexity is O(h).. we store the left most nodes and they
should be top of the stack for mininmum values... Then for next 
function, there can be right children for the popped node, thus we 
first add their right child, then again go left to store the min val node
in the stack.. This is a beautiful and elegant solution O(h) and O(n) time...
"""


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.root = root
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:

        res = self.stack.pop()

        curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
