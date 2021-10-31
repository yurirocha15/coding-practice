#!/usr/bin/env python

import pytest

"""
Test 2042. Check if Numbers Are Ascending in a Sentence
"""


@pytest.fixture(scope="session")
def init_variables_2042():
    from src.leetcode_2042_check_if_numbers_are_ascending_in_a_sentence import Solution

    solution = Solution()

    def _init_variables_2042():
        return solution

    yield _init_variables_2042


class TestClass2042:
    def test_solution_0(self, init_variables_2042):
        assert init_variables_2042().areNumbersAscending(
            "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
        )

    def test_solution_1(self, init_variables_2042):
        assert not init_variables_2042().areNumbersAscending("hello world 5 x 5")

    def test_solution_2(self, init_variables_2042):
        assert not init_variables_2042().areNumbersAscending(
            "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
        )

    def test_solution_3(self, init_variables_2042):
        assert init_variables_2042().areNumbersAscending("4 5 11 26")
