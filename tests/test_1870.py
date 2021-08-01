#!/usr/bin/env python

import pytest

"""
Test 1870. Minimum Speed to Arrive on Time
"""


@pytest.fixture(scope="session")
def init_variables_1870():
    from src.leetcode_1870_minimum_speed_to_arrive_on_time import Solution

    solution = Solution()

    def _init_variables_1870():
        return solution

    yield _init_variables_1870


class TestClass1870:
    def test_solution_0(self, init_variables_1870):
        assert init_variables_1870().minSpeedOnTime([1, 3, 2], 6) == 1

    def test_solution_1(self, init_variables_1870):
        assert init_variables_1870().minSpeedOnTime([1, 3, 2], 2.7) == 3

    def test_solution_2(self, init_variables_1870):
        assert init_variables_1870().minSpeedOnTime([1, 3, 2], 1.9) == -1
