#!/usr/bin/env python

import pytest

"""
Test 1806. Minimum Number of Operations to Reinitialize a Permutation
"""


@pytest.fixture(scope="session")
def init_variables_1806():
    from src.leetcode_1806_minimum_number_of_operations_to_reinitialize_a_permutation import Solution

    solution = Solution()

    def _init_variables_1806():
        return solution

    yield _init_variables_1806


class TestClass1806:
    def test_solution_0(self, init_variables_1806):
        assert init_variables_1806().reinitializePermutation(2) == 1

    def test_solution_1(self, init_variables_1806):
        assert init_variables_1806().reinitializePermutation(4) == 2

    def test_solution_2(self, init_variables_1806):
        assert init_variables_1806().reinitializePermutation(6) == 4
