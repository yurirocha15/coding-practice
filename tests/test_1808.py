#!/usr/bin/env python

import pytest

"""
Test 1808. Maximize Number of Nice Divisors
"""


@pytest.fixture(scope="session")
def init_variables_1808():
    from src.leetcode_1808_maximize_number_of_nice_divisors import Solution

    solution = Solution()

    def _init_variables_1808():
        return solution

    yield _init_variables_1808


class TestClass1808:
    def test_solution_0(self, init_variables_1808):
        assert init_variables_1808().maxNiceDivisors(5) == 6

    def test_solution_1(self, init_variables_1808):
        assert init_variables_1808().maxNiceDivisors(8) == 18
