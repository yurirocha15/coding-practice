#!/usr/bin/env python

import pytest

"""
Test 112. Path Sum
"""
from src.leetcode_112_path_sum import TreeNode


@pytest.fixture(scope="session")
def init_variables_112():
    from src.leetcode_112_path_sum import Solution

    solution = Solution()

    def _init_variables_112():
        return solution

    yield _init_variables_112


class TestClass112:
    def test_solution_0(self, init_variables_112):
        assert init_variables_112().hasPathSum(
            root=TreeNode(
                5,
                left=TreeNode(
                    4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))
                ),
                right=TreeNode(
                    8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1))
                ),
            ),
            targetSum=22,
        )

    def test_solution_1(self, init_variables_112):
        assert not init_variables_112().hasPathSum(
            TreeNode(1, TreeNode(2), TreeNode(3)), 5
        )

    def test_solution_2(self, init_variables_112):
        assert not init_variables_112().hasPathSum(TreeNode(1, TreeNode(2)), 0)
