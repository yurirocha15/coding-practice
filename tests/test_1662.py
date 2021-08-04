#!/usr/bin/env python

import pytest

"""
Test 1662. Check If Two String Arrays are Equivalent
"""


@pytest.fixture(scope="session")
def init_variables_1662():
    from src.leetcode_1662_check_if_two_string_arrays_are_equivalent import Solution

    solution = Solution()

    def _init_variables_1662():
        return solution

    yield _init_variables_1662


class TestClass1662:
    def test_solution_0(self, init_variables_1662):
        assert init_variables_1662().arrayStringsAreEqual(["ab", "c"], ["a", "bc"])

    def test_solution_1(self, init_variables_1662):
        assert not init_variables_1662().arrayStringsAreEqual(["a", "cb"], ["ab", "c"])

    def test_solution_2(self, init_variables_1662):
        assert init_variables_1662().arrayStringsAreEqual(
            ["abc", "d", "defg"], ["abcddefg"]
        )
