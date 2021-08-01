#!/usr/bin/env python

import pytest

"""
Test 1674. Minimum Moves to Make Array Complementary
"""


@pytest.fixture(scope="session")
def init_variables_1674():
    from src.leetcode_1674_minimum_moves_to_make_array_complementary import Solution

    solution = Solution()

    def _init_variables_1674():
        return solution

    yield _init_variables_1674


class TestClass1674:
    def test_solution_0(self, init_variables_1674):
        assert init_variables_1674().minMoves([1, 2, 4, 3], 4) == 1

    def test_solution_1(self, init_variables_1674):
        assert init_variables_1674().minMoves([1, 2, 2, 1], 2) == 2

    def test_solution_2(self, init_variables_1674):
        assert init_variables_1674().minMoves([1, 2, 1, 2], 2) == 0
