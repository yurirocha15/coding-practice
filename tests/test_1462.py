#!/usr/bin/env python

import pytest

"""
Test 1462. Course Schedule IV
"""


@pytest.fixture(scope="session")
def init_variables_1462():
    from src.leetcode_1462_course_schedule_iv import Solution

    solution = Solution()

    def _init_variables_1462():
        return solution

    yield _init_variables_1462


class TestClass1462:
    def test_solution_0(self, init_variables_1462):
        assert init_variables_1462().checkIfPrerequisite(
            2, [[1, 0]], [[0, 1], [1, 0]]
        ) == [False, True]

    def test_solution_1(self, init_variables_1462):
        assert init_variables_1462().checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [
            False,
            False,
        ]

    def test_solution_2(self, init_variables_1462):
        assert init_variables_1462().checkIfPrerequisite(
            3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]
        ) == [True, True]
