#!/usr/bin/env python

import pytest

"""
Test 1930. Unique Length-3 Palindromic Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_1930():
    from src.leetcode_1930_unique_length_3_palindromic_subsequences import Solution

    solution = Solution()

    def _init_variables_1930():
        return solution

    yield _init_variables_1930


class TestClass1930:
    def test_solution_0(self, init_variables_1930):
        assert init_variables_1930().countPalindromicSubsequence("aabca") == 3

    def test_solution_1(self, init_variables_1930):
        assert init_variables_1930().countPalindromicSubsequence("adc") == 0

    def test_solution_2(self, init_variables_1930):
        assert init_variables_1930().countPalindromicSubsequence("bbcbaba") == 4
