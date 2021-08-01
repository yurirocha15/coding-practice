#!/usr/bin/env python

import pytest

"""
Test 1744. Can You Eat Your Favorite Candy on Your Favorite Day?
"""


@pytest.fixture(scope="session")
def init_variables_1744():
    from src.leetcode_1744_can_you_eat_your_favorite_candy_on_your_favorite_day import Solution

    solution = Solution()

    def _init_variables_1744():
        return solution

    yield _init_variables_1744


class TestClass1744:
    def test_solution_0(self, init_variables_1744):
        assert init_variables_1744().canEat(
            [7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
        ) == [True, False, True]

    def test_solution_1(self, init_variables_1744):
        assert (
            init_variables_1744().canEat(
                [5, 2, 6, 4, 1],
                [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]],
            )
            == [False, True, True, False, False]
        )
