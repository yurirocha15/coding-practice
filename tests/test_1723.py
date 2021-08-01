#!/usr/bin/env python

import pytest

"""
Test 1723. Find Minimum Time to Finish All Jobs
"""


@pytest.fixture(scope="session")
def init_variables_1723():
    from src.leetcode_1723_find_minimum_time_to_finish_all_jobs import Solution

    solution = Solution()

    def _init_variables_1723():
        return solution

    yield _init_variables_1723


class TestClass1723:
    def test_solution_0(self, init_variables_1723):
        assert init_variables_1723().minimumTimeRequired([3, 2, 3], 3) == 3

    def test_solution_1(self, init_variables_1723):
        assert init_variables_1723().minimumTimeRequired([1, 2, 4, 7, 8], 2) == 11
