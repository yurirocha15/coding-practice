#!/usr/bin/env python

import pytest

"""
Test 1854. Maximum Population Year
"""


@pytest.fixture(scope="session")
def init_variables_1854():
    from src.leetcode_1854_maximum_population_year import Solution

    solution = Solution()

    def _init_variables_1854():
        return solution

    yield _init_variables_1854


class TestClass1854:
    def test_solution_0(self, init_variables_1854):
        assert (
            init_variables_1854().maximumPopulation([[1993, 1999], [2000, 2010]])
            == 1993
        )

    def test_solution_1(self, init_variables_1854):
        assert (
            init_variables_1854().maximumPopulation(
                [[1950, 1961], [1960, 1971], [1970, 1981]]
            )
            == 1960
        )
