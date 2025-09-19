"""
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).


Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true


Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.process_tree(root.left, True) == self.process_tree(
            root.right, False
        )

    def process_tree(self, root: TreeNode, left: bool) -> list:
        result = []

        dq = deque([root])

        while dq:
            cur = dq.popleft()
            if cur:
                result.append(cur.val)
                dq.extend([cur.left, cur.right] if left else [cur.right, cur.left])
            else:
                result.append(None)

        return result


class SolutionRecur:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.process_tree(root.left, True) == self.process_tree(
            root.right, False
        )

    def process_tree(self, root: Optional[TreeNode], left: bool) -> list:
        if not root:
            return [None]

        return (
            [root.val]
            + self.process_tree(root.left, left)
            + self.process_tree(root.right, left)
            if left
            else [root.val]
            + self.process_tree(root.right, left)
            + self.process_tree(root.left, left)
        )
