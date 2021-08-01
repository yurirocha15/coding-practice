#!/usr/bin/env python

import pytest

"""
Test 1695. Maximum Erasure Value
"""


@pytest.fixture(scope="session")
def init_variables_1695():
    from src.leetcode_1695_maximum_erasure_value import Solution

    solution = Solution()

    def _init_variables_1695():
        return solution

    yield _init_variables_1695


class TestClass1695:
    def test_solution_0(self, init_variables_1695):
        assert init_variables_1695().maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17

    def test_solution_1(self, init_variables_1695):
        assert (
            init_variables_1695().maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5])
            == 8
        )
