#!/usr/bin/env python

import pytest

"""
Test 1935. Maximum Number of Words You Can Type
"""


@pytest.fixture(scope="session")
def init_variables_1935():
    from src.leetcode_1935_maximum_number_of_words_you_can_type import Solution

    solution = Solution()

    def _init_variables_1935():
        return solution

    yield _init_variables_1935


class TestClass1935:
    def test_solution_0(self, init_variables_1935):
        assert init_variables_1935().canBeTypedWords("hello world", "ad") == 1

    def test_solution_1(self, init_variables_1935):
        assert init_variables_1935().canBeTypedWords("leet code", "lt") == 1

    def test_solution_2(self, init_variables_1935):
        assert init_variables_1935().canBeTypedWords("leet code", "e") == 0
