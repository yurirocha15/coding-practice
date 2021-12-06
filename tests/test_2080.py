#!/usr/bin/env python

import pytest

"""
Test 2080. Range Frequency Queries
"""


@pytest.fixture(scope="session")
def init_variables_2080():
    from src.leetcode_2080_range_frequency_queries import RangeFreqQuery

    solution = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])

    def _init_variables_2080():
        return solution

    yield _init_variables_2080


class TestClass2080:
    def test_solution_0(self, init_variables_2080):
        assert init_variables_2080().query(1, 2, 4) == 1
        assert init_variables_2080().query(0, 11, 33) == 2
