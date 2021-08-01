#!/usr/bin/env python

import pytest

"""
Test 1838. Frequency of the Most Frequent Element
"""


@pytest.fixture(scope="session")
def init_variables_1838():
    from src.leetcode_1838_frequency_of_the_most_frequent_element import Solution

    solution = Solution()

    def _init_variables_1838():
        return solution

    yield _init_variables_1838


class TestClass1838:
    def test_solution_0(self, init_variables_1838):
        assert init_variables_1838().maxFrequency([1, 2, 4], 5) == 3

    def test_solution_1(self, init_variables_1838):
        assert init_variables_1838().maxFrequency([1, 4, 8, 13], 5) == 2

    def test_solution_2(self, init_variables_1838):
        assert init_variables_1838().maxFrequency([3, 9, 6], 2) == 1
