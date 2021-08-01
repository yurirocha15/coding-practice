#!/usr/bin/env python

import pytest

"""
Test 1663. Smallest String With A Given Numeric Value
"""


@pytest.fixture(scope="session")
def init_variables_1663():
    from src.leetcode_1663_smallest_string_with_a_given_numeric_value import Solution

    solution = Solution()

    def _init_variables_1663():
        return solution

    yield _init_variables_1663


class TestClass1663:
    def test_solution_0(self, init_variables_1663):
        assert init_variables_1663().getSmallestString(3, 27) == "aay"

    def test_solution_1(self, init_variables_1663):
        assert init_variables_1663().getSmallestString(5, 73) == "aaszz"
