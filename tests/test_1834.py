#!/usr/bin/env python

import pytest

"""
Test 1834. Single-Threaded CPU
"""


@pytest.fixture(scope="session")
def init_variables_1834():
    from src.leetcode_1834_single_threaded_cpu import Solution

    solution = Solution()

    def _init_variables_1834():
        return solution

    yield _init_variables_1834


class TestClass1834:
    def test_solution_0(self, init_variables_1834):
        assert init_variables_1834().getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [
            0,
            2,
            3,
            1,
        ]

    def test_solution_1(self, init_variables_1834):
        assert init_variables_1834().getOrder(
            [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
        ) == [4, 3, 2, 0, 1]
