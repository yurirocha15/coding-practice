#!/usr/bin/env python

import pytest

"""
Test 2045. Second Minimum Time to Reach Destination
"""


@pytest.fixture(scope="session")
def init_variables_2045():
    from src.leetcode_2045_second_minimum_time_to_reach_destination import Solution

    solution = Solution()

    def _init_variables_2045():
        return solution

    yield _init_variables_2045


class TestClass2045:
    def test_solution_0(self, init_variables_2045):
        assert (
            init_variables_2045().secondMinimum(
                5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5
            )
            == 13
        )

    def test_solution_1(self, init_variables_2045):
        assert init_variables_2045().secondMinimum(2, [[1, 2]], 3, 2) == 11

    def test_solution_1(self, init_variables_2045):
        assert (
            init_variables_2045().secondMinimum(
                6, [[1, 2], [1, 3], [2, 4], [3, 5], [5, 4], [4, 6]], 3, 100
            )
            == 12
        )
