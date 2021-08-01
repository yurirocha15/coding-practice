# @l2g 113 python3
# [113] Path Sum II
# Difficulty: Medium
# https://leetcode.com/problems/path-sum-ii
#
# Given the root of a binary tree and an integer targetSum,
# return all root-to-leaf paths where each path's sum equals targetSum.
# A leaf is a node with no children.
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
# Example 3:
#
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
#
from collections import deque
from typing import Deque, List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        dq: Deque[Tuple[int, List[int], TreeNode]] = deque()
        ret: List[List[int]] = []
        if root:
            dq.append((0, [], root))
        while dq:
            curr_sum, curr_path, node = dq.pop()
            curr_sum += node.val
            curr_path.append(node.val)
            if curr_sum == targetSum and not node.left and not node.right:
                ret.append(curr_path)
            if node.left:
                dq.append((curr_sum, list(curr_path), node.left))
            if node.right:
                dq.append((curr_sum, list(curr_path), node.right))
        print(ret)
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_113.py")])
