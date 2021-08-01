#!/usr/bin/env python

import pytest

"""
Test 1899. Merge Triplets to Form Target Triplet
"""


@pytest.fixture(scope="session")
def init_variables_1899():
    from src.leetcode_1899_merge_triplets_to_form_target_triplet import Solution

    solution = Solution()

    def _init_variables_1899():
        return solution

    yield _init_variables_1899


class TestClass1899:
    def test_solution_0(self, init_variables_1899):
        assert init_variables_1899().mergeTriplets(
            [[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]
        )

    def test_solution_1(self, init_variables_1899):
        assert init_variables_1899().mergeTriplets([[1, 3, 4], [2, 5, 8]], [2, 5, 8])

    def test_solution_2(self, init_variables_1899):
        assert init_variables_1899().mergeTriplets(
            [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]
        )

    def test_solution_3(self, init_variables_1899):
        assert not init_variables_1899().mergeTriplets(
            [[3, 4, 5], [4, 5, 6]], [3, 2, 5]
        )
