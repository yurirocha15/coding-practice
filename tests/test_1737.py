#!/usr/bin/env python

import pytest

"""
Test 1737. Change Minimum Characters to Satisfy One of Three Conditions
"""


@pytest.fixture(scope="session")
def init_variables_1737():
    from src.leetcode_1737_change_minimum_characters_to_satisfy_one_of_three_conditions import Solution

    solution = Solution()

    def _init_variables_1737():
        return solution

    yield _init_variables_1737


class TestClass1737:
    def test_solution_0(self, init_variables_1737):
        assert init_variables_1737().minCharacters("aba", "caa") == 2

    def test_solution_1(self, init_variables_1737):
        assert init_variables_1737().minCharacters("dabadd", "cda") == 3
