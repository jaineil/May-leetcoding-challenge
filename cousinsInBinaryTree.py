# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The idea is to apply DFS on left and right subtree of the root 
# To get info for x & y (ie. depth and parent)

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        xInfo = []
        yInfo = []
        
        self.dfs(root, x, y, 0, None, xInfo, yInfo)
        return xInfo[0][0] == yInfo[0][0] and xInfo[0][1] != yInfo[0][1]
        
    def dfs(self, root, x, y, depth, parent, xInfo, yInfo):
        if root is None:
            return None
        if root.val == x:
            xInfo.append((depth, parent))
        if root.val == y:
            yInfo.append((depth, parent))
            
        self.dfs(root.left, x, y, depth+1, root, xInfo, yInfo)
        self.dfs(root.right, x, y, depth+1, root, xInfo, yInfo)