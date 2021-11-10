#!/usr/bin/env python

import pytest

"""
Test 2049. Count Nodes With the Highest Score
"""


@pytest.fixture(scope="session")
def init_variables_2049():
    from src.leetcode_2049_count_nodes_with_the_highest_score import Solution

    solution = Solution()

    def _init_variables_2049():
        return solution

    yield _init_variables_2049


class TestClass2049:
    def test_solution_0(self, init_variables_2049):
        assert init_variables_2049().countHighestScoreNodes([-1, 2, 0, 2, 0]) == 3

    def test_solution_1(self, init_variables_2049):
        assert init_variables_2049().countHighestScoreNodes([-1, 2, 0]) == 2
