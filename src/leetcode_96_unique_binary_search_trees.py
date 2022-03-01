# @l2g 96 python3
# [96] Unique Binary Search Trees
# Difficulty: Medium
# https://leetcode.com/problems/unique-binary-search-trees
#
# Given an integer n,
# return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
# Example 2:
#
# Input: n = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 19
#
#


class Solution:
    def numTrees(self, n: int) -> int:
        catalan_number = 1
        for i in range(1, n):
            catalan_number = 2 * (2 * i + 1) * catalan_number // (i + 2)
        return catalan_number


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_96.py")])
