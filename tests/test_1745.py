#!/usr/bin/env python

import pytest

"""
Test 1745. Palindrome Partitioning IV
"""


@pytest.fixture(scope="session")
def init_variables_1745():
    from src.leetcode_1745_palindrome_partitioning_iv import Solution

    solution = Solution()

    def _init_variables_1745():
        return solution

    yield _init_variables_1745


class TestClass1745:
    def test_solution_0(self, init_variables_1745):
        assert init_variables_1745().checkPartitioning("abcbdd")

    def test_solution_1(self, init_variables_1745):
        assert not init_variables_1745().checkPartitioning("bcbddxy")
