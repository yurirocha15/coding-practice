#!/usr/bin/env python

import pytest

"""
Test 1771. Maximize Palindrome Length From Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_1771():
    from src.leetcode_1771_maximize_palindrome_length_from_subsequences import Solution

    solution = Solution()

    def _init_variables_1771():
        return solution

    yield _init_variables_1771


class TestClass1771:
    def test_solution_0(self, init_variables_1771):
        assert init_variables_1771().longestPalindrome("cacb", "cbba") == 5

    def test_solution_1(self, init_variables_1771):
        assert init_variables_1771().longestPalindrome("ab", "ab") == 3

    def test_solution_2(self, init_variables_1771):
        assert init_variables_1771().longestPalindrome("aa", "bb") == 0
