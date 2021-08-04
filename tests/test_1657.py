#!/usr/bin/env python

import pytest

"""
Test 1657. Determine if Two Strings Are Close
"""


@pytest.fixture(scope="session")
def init_variables_1657():
    from src.leetcode_1657_determine_if_two_strings_are_close import Solution

    solution = Solution()

    def _init_variables_1657():
        return solution

    yield _init_variables_1657


class TestClass1657:
    def test_solution_0(self, init_variables_1657):
        assert init_variables_1657().closeStrings("abc", "bca")

    def test_solution_1(self, init_variables_1657):
        assert not init_variables_1657().closeStrings("a", "aa")

    def test_solution_2(self, init_variables_1657):
        assert init_variables_1657().closeStrings("cabbba", "abbccc")

    def test_solution_3(self, init_variables_1657):
        assert not init_variables_1657().closeStrings("cabbba", "aabbss")
