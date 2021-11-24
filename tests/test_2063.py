#!/usr/bin/env python

import pytest

"""
Test 2063. Vowels of All Substrings
"""


@pytest.fixture(scope="session")
def init_variables_2063():
    from src.leetcode_2063_vowels_of_all_substrings import Solution

    solution = Solution()

    def _init_variables_2063():
        return solution

    yield _init_variables_2063


class TestClass2063:
    def test_solution_0(self, init_variables_2063):
        assert init_variables_2063().countVowels("aba") == 6

    def test_solution_1(self, init_variables_2063):
        assert init_variables_2063().countVowels("abc") == 3

    def test_solution_2(self, init_variables_2063):
        assert init_variables_2063().countVowels("ltcd") == 0

    def test_solution_3(self, init_variables_2063):
        assert init_variables_2063().countVowels("noosabasboosa") == 237
