#!/usr/bin/env python

import pytest

"""
Test 2062. Count Vowel Substrings of a String
"""


@pytest.fixture(scope="session")
def init_variables_2062():
    from src.leetcode_2062_count_vowel_substrings_of_a_string import Solution

    solution = Solution()

    def _init_variables_2062():
        return solution

    yield _init_variables_2062


class TestClass2062:
    def test_solution_0(self, init_variables_2062):
        assert init_variables_2062().countVowelSubstrings("aeiouu") == 2

    def test_solution_1(self, init_variables_2062):
        assert init_variables_2062().countVowelSubstrings("unicornarihan") == 0

    def test_solution_2(self, init_variables_2062):
        assert init_variables_2062().countVowelSubstrings("cuaieuouac") == 7

    def test_solution_3(self, init_variables_2062):
        assert init_variables_2062().countVowelSubstrings("bbaeixoubb") == 0
