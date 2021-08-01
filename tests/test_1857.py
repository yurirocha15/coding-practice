#!/usr/bin/env python

import pytest

"""
Test 1857. Largest Color Value in a Directed Graph
"""


@pytest.fixture(scope="session")
def init_variables_1857():
    from src.leetcode_1857_largest_color_value_in_a_directed_graph import Solution

    solution = Solution()

    def _init_variables_1857():
        return solution

    yield _init_variables_1857


class TestClass1857:
    def test_solution_0(self, init_variables_1857):
        assert (
            init_variables_1857().largestPathValue(
                "abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]
            )
            == 3
        )

    def test_solution_1(self, init_variables_1857):
        assert init_variables_1857().largestPathValue("a", [[0, 0]]) == -1
