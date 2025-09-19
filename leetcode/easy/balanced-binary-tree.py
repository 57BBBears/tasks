"""
Given a binary tree, determine if it is height-balanced.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true


Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_depth(root) != -1

    def get_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.get_depth(root.left)

        if left_depth == -1:
            return -1

        right_depth = self.get_depth(root.right)

        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return 1 + max(left_depth, right_depth)
