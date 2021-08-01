#!/usr/bin/env python

import pytest

"""
Test 1743. Restore the Array From Adjacent Pairs
"""


@pytest.fixture(scope="session")
def init_variables_1743():
    from src.leetcode_1743_restore_the_array_from_adjacent_pairs import Solution

    solution = Solution()

    def _init_variables_1743():
        return solution

    yield _init_variables_1743


class TestClass1743:
    def test_solution_0(self, init_variables_1743):
        assert init_variables_1743().restoreArray([[2, 1], [3, 4], [3, 2]]) == [
            1,
            2,
            3,
            4,
        ]

    def test_solution_1(self, init_variables_1743):
        assert init_variables_1743().restoreArray([[4, -2], [1, 4], [-3, 1]]) == [
            -2,
            4,
            1,
            -3,
        ]

    def test_solution_2(self, init_variables_1743):
        assert init_variables_1743().restoreArray([[100000, -100000]]) == [
            100000,
            -100000,
        ]
