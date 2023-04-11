"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
Now following this solution. - 
https://www.youtube.com/watch?v=U4hFQCa1Cq0

This is the best code!!! refer to - https://www.youtube.com/watch?v=30Bqbk-Vk3Q
Also do a dru run then u will get an idea how simple it actually is!1!!!


"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        current = root
        leftChildPointer = root.left if root else None

        while current and leftChildPointer:

            # Connect Left child to right child
            current.left.next = current.right

            # Check if right can be connected further
            if current.next:
                current.right.next = current.next.left

            # Advance current pointer to its next
            current = current.next

            # Check if it is none, point it to leftChildPointer
            if current is None:
                current = leftChildPointer
                leftChildPointer = current.left

        return root
