#!/usr/bin/env python

import pytest

"""
Test 1792. Maximum Average Pass Ratio
"""


@pytest.fixture(scope="session")
def init_variables_1792():
    from src.leetcode_1792_maximum_average_pass_ratio import Solution

    solution = Solution()

    def _init_variables_1792():
        return solution

    yield _init_variables_1792


class TestClass1792:
    def test_solution_0(self, init_variables_1792):
        assert (
            init_variables_1792().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2)
            == 0.78333
        )

    def test_solution_1(self, init_variables_1792):
        assert (
            init_variables_1792().maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4)
            == 0.53485
        )
