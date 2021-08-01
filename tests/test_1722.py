#!/usr/bin/env python

import pytest

"""
Test 1722. Minimize Hamming Distance After Swap Operations
"""


@pytest.fixture(scope="session")
def init_variables_1722():
    from src.leetcode_1722_minimize_hamming_distance_after_swap_operations import Solution

    solution = Solution()

    def _init_variables_1722():
        return solution

    yield _init_variables_1722


class TestClass1722:
    def test_solution_0(self, init_variables_1722):
        assert (
            init_variables_1722().minimumHammingDistance(
                [1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]
            )
            == 1
        )

    def test_solution_1(self, init_variables_1722):
        assert (
            init_variables_1722().minimumHammingDistance([1, 2, 3, 4], [1, 3, 2, 4], [])
            == 2
        )

    def test_solution_2(self, init_variables_1722):
        assert (
            init_variables_1722().minimumHammingDistance(
                [5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]]
            )
            == 0
        )
