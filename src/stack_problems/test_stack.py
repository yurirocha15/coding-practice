#!/usr/bin/env python

import pytest

"""
Test 1673: find_the_most_competitive_subsequence
"""


@pytest.fixture(scope="session")
def init_variables_1673():
    from src.stack_problems.find_the_most_competitive_subsequence import Solution

    solution = Solution()

    def _init_variables_1673():
        return solution

    yield _init_variables_1673


class TestClass1673:
    def test_solution_0(self, init_variables_1673):
        assert init_variables_1673().most_competitive([3, 5, 2, 6], 2) == [2, 6]

    def test_solution_1(self, init_variables_1673):
        assert init_variables_1673().most_competitive([2, 4, 3, 3, 5, 4, 9, 6], 4) == [
            2,
            3,
            3,
            4,
        ]
