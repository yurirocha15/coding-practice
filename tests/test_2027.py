#!/usr/bin/env python

import pytest

"""
Test 2027. Minimum Moves to Convert String
"""


@pytest.fixture(scope="session")
def init_variables_2027():
    from src.leetcode_2027_minimum_moves_to_convert_string import Solution

    solution = Solution()

    def _init_variables_2027():
        return solution

    yield _init_variables_2027


class TestClass2027:
    def test_solution_0(self, init_variables_2027):
        assert init_variables_2027().minimumMoves("XXX") == 1

    def test_solution_1(self, init_variables_2027):
        assert init_variables_2027().minimumMoves("XXOX") == 2

    def test_solution_2(self, init_variables_2027):
        assert init_variables_2027().minimumMoves("OOOO") == 0
