#!/usr/bin/env python

import pytest

"""
Test 207. Course Schedule
"""


@pytest.fixture(scope="session")
def init_variables_207():
    from src.leetcode_207_course_schedule import Solution

    solution = Solution()

    def _init_variables_207():
        return solution

    yield _init_variables_207


class TestClass207:
    def test_solution_0(self, init_variables_207):
        assert init_variables_207().canFinish(2, [[1, 0]])

    def test_solution_1(self, init_variables_207):
        assert not init_variables_207().canFinish(2, [[1, 0], [0, 1]])
