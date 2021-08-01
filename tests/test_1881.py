#!/usr/bin/env python

import pytest

"""
Test 1881. Maximum Value after Insertion
"""


@pytest.fixture(scope="session")
def init_variables_1881():
    from src.leetcode_1881_maximum_value_after_insertion import Solution

    solution = Solution()

    def _init_variables_1881():
        return solution

    yield _init_variables_1881


class TestClass1881:
    def test_solution_0(self, init_variables_1881):
        assert init_variables_1881().maxValue("99", 9) == "999"

    def test_solution_1(self, init_variables_1881):
        assert init_variables_1881().maxValue("-13", 2) == "-123"
