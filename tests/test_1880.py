#!/usr/bin/env python

import pytest

"""
Test 1880. Check if Word Equals Summation of Two Words
"""


@pytest.fixture(scope="session")
def init_variables_1880():
    from src.leetcode_1880_check_if_word_equals_summation_of_two_words import Solution

    solution = Solution()

    def _init_variables_1880():
        return solution

    yield _init_variables_1880


class TestClass1880:
    def test_solution_0(self, init_variables_1880):
        assert init_variables_1880().isSumEqual("acb", "cba", "cdb")

    def test_solution_1(self, init_variables_1880):
        assert not init_variables_1880().isSumEqual("aaa", "a", "aab")

    def test_solution_2(self, init_variables_1880):
        assert init_variables_1880().isSumEqual("aaa", "a", "aaaa")
