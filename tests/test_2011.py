#!/usr/bin/env python

import pytest

"""
Test 2011. Final Value of Variable After Performing Operations
"""


@pytest.fixture(scope="session")
def init_variables_2011():
    from src.leetcode_2011_final_value_of_variable_after_performing_operations import Solution

    solution = Solution()

    def _init_variables_2011():
        return solution

    yield _init_variables_2011


class TestClass2011:
    def test_solution_0(self, init_variables_2011):
        assert (
            init_variables_2011().finalValueAfterOperations(["--X", "X++", "X++"]) == 1
        )

    def test_solution_1(self, init_variables_2011):
        assert (
            init_variables_2011().finalValueAfterOperations(["++X", "++X", "X++"]) == 3
        )

    def test_solution_2(self, init_variables_2011):
        assert (
            init_variables_2011().finalValueAfterOperations(
                ["X++", "++X", "--X", "X--"]
            )
            == 0
        )
