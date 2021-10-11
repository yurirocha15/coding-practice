#!/usr/bin/env python

import pytest

"""
Test 2018. Check if Word Can Be Placed In Crossword
"""


@pytest.fixture(scope="session")
def init_variables_2018():
    from src.leetcode_2018_check_if_word_can_be_placed_in_crossword import Solution

    solution = Solution()

    def _init_variables_2018():
        return solution

    yield _init_variables_2018


class TestClass2018:
    def test_solution_0(self, init_variables_2018):
        assert init_variables_2018().placeWordInCrossword(
            [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "abc"
        )

    def test_solution_1(self, init_variables_2018):
        assert not init_variables_2018().placeWordInCrossword(
            [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], "ac"
        )

    def test_solution_2(self, init_variables_2018):
        assert init_variables_2018().placeWordInCrossword(
            [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], "ca"
        )
