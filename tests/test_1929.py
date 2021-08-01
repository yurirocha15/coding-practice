#!/usr/bin/env python

import pytest

"""
Test 1929. Concatenation of Array
"""


@pytest.fixture(scope="session")
def init_variables_1929():
    from src.leetcode_1929_concatenation_of_array import Solution

    solution = Solution()

    def _init_variables_1929():
        return solution

    yield _init_variables_1929


class TestClass1929:
    def test_solution_0(self, init_variables_1929):
        assert init_variables_1929().getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]

    def test_solution_1(self, init_variables_1929):
        assert init_variables_1929().getConcatenation([1, 3, 2, 1]) == [
            1,
            3,
            2,
            1,
            1,
            3,
            2,
            1,
        ]
