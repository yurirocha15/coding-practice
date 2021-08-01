#!/usr/bin/env python

import pytest

"""
Test 1839. Longest Substring Of All Vowels in Order
"""


@pytest.fixture(scope="session")
def init_variables_1839():
    from src.leetcode_1839_longest_substring_of_all_vowels_in_order import Solution

    solution = Solution()

    def _init_variables_1839():
        return solution

    yield _init_variables_1839


class TestClass1839:
    def test_solution_0(self, init_variables_1839):
        assert (
            init_variables_1839().longestBeautifulSubstring(
                "aeiaaioaaaaeiiiiouuuooaauuaeiu"
            )
            == 13
        )

    def test_solution_1(self, init_variables_1839):
        assert (
            init_variables_1839().longestBeautifulSubstring("aeeeiiiioooauuuaeiou") == 5
        )

    def test_solution_2(self, init_variables_1839):
        assert init_variables_1839().longestBeautifulSubstring("a") == 0
