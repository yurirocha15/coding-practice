#!/usr/bin/env python

import pytest

"""
Test 1736. Latest Time by Replacing Hidden Digits
"""


@pytest.fixture(scope="session")
def init_variables_1736():
    from src.leetcode_1736_latest_time_by_replacing_hidden_digits import Solution

    solution = Solution()

    def _init_variables_1736():
        return solution

    yield _init_variables_1736


class TestClass1736:
    def test_solution_0(self, init_variables_1736):
        assert init_variables_1736().maximumTime("2?:?0") == "23:50"

    def test_solution_1(self, init_variables_1736):
        assert init_variables_1736().maximumTime("0?:3?") == "09:39"

    def test_solution_2(self, init_variables_1736):
        assert init_variables_1736().maximumTime("1?:22") == "19:22"
