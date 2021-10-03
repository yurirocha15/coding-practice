#!/usr/bin/env python

import pytest

"""
Test 2012. Sum of Beauty in the Array
"""


@pytest.fixture(scope="session")
def init_variables_2012():
    from src.leetcode_2012_sum_of_beauty_in_the_array import Solution

    solution = Solution()

    def _init_variables_2012():
        return solution

    yield _init_variables_2012


class TestClass2012:
    def test_solution_0(self, init_variables_2012):
        assert init_variables_2012().sumOfBeauties([1, 2, 3]) == 2

    def test_solution_1(self, init_variables_2012):
        assert init_variables_2012().sumOfBeauties([2, 4, 6, 4]) == 1

    def test_solution_2(self, init_variables_2012):
        assert init_variables_2012().sumOfBeauties([3, 2, 1]) == 0
