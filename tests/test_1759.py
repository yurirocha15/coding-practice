#!/usr/bin/env python

import pytest

"""
Test 1759. Count Number of Homogenous Substrings
"""


@pytest.fixture(scope="session")
def init_variables_1759():
    from src.leetcode_1759_count_number_of_homogenous_substrings import Solution

    solution = Solution()

    def _init_variables_1759():
        return solution

    yield _init_variables_1759


class TestClass1759:
    def test_solution_0(self, init_variables_1759):
        assert init_variables_1759().countHomogenous("abbcccaa") == 13

    def test_solution_1(self, init_variables_1759):
        assert init_variables_1759().countHomogenous("xy") == 2

    def test_solution_2(self, init_variables_1759):
        assert init_variables_1759().countHomogenous("zzzzz") == 15
