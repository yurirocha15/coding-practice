#!/usr/bin/env python

import pytest

"""
Test 113. Path Sum II
"""
from src.leetcode_113_path_sum_ii import TreeNode


@pytest.fixture(scope="session")
def init_variables_113():
    from src.leetcode_113_path_sum_ii import Solution

    solution = Solution()

    def _init_variables_113():
        return solution

    yield _init_variables_113


class TestClass113:
    def test_solution_0(self, init_variables_113):
        assert (
            sorted(
                init_variables_113().pathSum(
                    TreeNode(
                        5,
                        left=TreeNode(
                            4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))
                        ),
                        right=TreeNode(
                            8,
                            left=TreeNode(13),
                            right=TreeNode(4, left=TreeNode(5), right=TreeNode(1)),
                        ),
                    ),
                    22,
                )
            )
            == [[5, 4, 11, 2], [5, 8, 4, 5]]
        )

    def test_solution_1(self, init_variables_113):
        assert (
            init_variables_113().pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5) == []
        )

    def test_solution_2(self, init_variables_113):
        assert init_variables_113().pathSum(TreeNode(1, TreeNode(2)), 0) == []
