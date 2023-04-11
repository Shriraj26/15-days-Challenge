# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Neetcode === leetcode
Constrct a string of the tree node values and add # wherever it is None
the deserialize function is like magic, it has a dfs function that 
does not take any args, like I have not seen it before thats it 
is new for me!! if u encounter a #, then return None, but before that
increment i 
And in normal calls, increment i, then attach left and rifht
subtrees to it
WOW
Just do a dry run and you will get the ans... The lEft and right calls a
parent makes to its children get the appropriate index... thus u dont need too
Worry!!!
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = []

        def dfs(root):
            if root is None:
                result.append("#")
                return

            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        treeArr = data.split(",")

        def dfs():
            if treeArr[self.i] == "#":
                self.i += 1
                return None

            # make a tree node
            node = TreeNode(int(treeArr[self.i]))
            # increment i to get its children
            self.i += 1
            # attach left and right subtrees
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
