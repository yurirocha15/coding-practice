#!/usr/bin/env python

import pytest

"""
Test 2081. Sum of k-Mirror Numbers
"""


@pytest.fixture(scope="session")
def init_variables_2081():
    from src.leetcode_2081_sum_of_k_mirror_numbers import Solution

    solution = Solution()

    def _init_variables_2081():
        return solution

    yield _init_variables_2081


class TestClass2081:
    def test_solution_0(self, init_variables_2081):
        assert init_variables_2081().kMirror(2, 5) == 25

    def test_solution_1(self, init_variables_2081):
        assert init_variables_2081().kMirror(3, 7) == 499

    def test_solution_2(self, init_variables_2081):
        assert init_variables_2081().kMirror(7, 17) == 20379000
