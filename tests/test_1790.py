#!/usr/bin/env python

import pytest

"""
Test 1790. Check if One String Swap Can Make Strings Equal
"""


@pytest.fixture(scope="session")
def init_variables_1790():
    from src.leetcode_1790_check_if_one_string_swap_can_make_strings_equal import Solution

    solution = Solution()

    def _init_variables_1790():
        return solution

    yield _init_variables_1790


class TestClass1790:
    def test_solution_0(self, init_variables_1790):
        assert init_variables_1790().areAlmostEqual("bank", "kanb")

    def test_solution_1(self, init_variables_1790):
        assert not init_variables_1790().areAlmostEqual("attack", "defend")

    def test_solution_2(self, init_variables_1790):
        assert init_variables_1790().areAlmostEqual("kelb", "kelb")

    def test_solution_3(self, init_variables_1790):
        assert not init_variables_1790().areAlmostEqual("abcd", "dcba")
