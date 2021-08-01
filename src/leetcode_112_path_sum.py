# @l2g 112 python3
# [112] Path Sum
# Difficulty: Easy
# https://leetcode.com/problems/path-sum
#
# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
#
# Example 3:
#
# Input: root = [1,2], targetSum = 0
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        dq = deque()
        if root:
            dq.append((0, root))
        while dq:
            curr_sum, node = dq.pop()
            curr_sum += node.val
            if curr_sum == targetSum and not node.left and not node.right:
                return True
            if node.left:
                dq.append((curr_sum, node.left))
            if node.right:
                dq.append((curr_sum, node.right))
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_112.py")])
