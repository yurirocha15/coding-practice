#!/usr/bin/env python

import pytest

"""
Test 1758. Minimum Changes To Make Alternating Binary String
"""


@pytest.fixture(scope="session")
def init_variables_1758():
    from src.leetcode_1758_minimum_changes_to_make_alternating_binary_string import Solution

    solution = Solution()

    def _init_variables_1758():
        return solution

    yield _init_variables_1758


class TestClass1758:
    def test_solution_0(self, init_variables_1758):
        assert init_variables_1758().minOperations("0100") == 1

    def test_solution_1(self, init_variables_1758):
        assert init_variables_1758().minOperations("10") == 0

    def test_solution_2(self, init_variables_1758):
        assert init_variables_1758().minOperations("1111") == 2
