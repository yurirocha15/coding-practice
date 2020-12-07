#!/usr/bin/env python

import pytest

"""
Test 1647: minimum_deletions_to_make_character_frequencies_unique
"""


@pytest.fixture(scope="session")
def init_variables_1647():
    from src.sort_problems.minimum_deletions_to_make_character_frequencies_unique import Solution

    solution = Solution()

    def _init_variables_1647():
        return solution

    yield _init_variables_1647


class TestClass1647:
    def test_solution_0(self, init_variables_1647):
        assert init_variables_1647().min_deletions("aab") == 0

    def test_solution_1(self, init_variables_1647):
        assert init_variables_1647().min_deletions("aaabbbcc") == 2

    def test_solution_2(self, init_variables_1647):
        assert init_variables_1647().min_deletions("ceabaacb") == 2


"""
Test 1648: sell_diminishing_valued_colored_balls
"""


@pytest.fixture(scope="session")
def init_variables_1648():
    from src.sort_problems.sell_diminishing_valued_colored_balls import Solution

    solution = Solution()

    def _init_variables_1648():
        return solution

    yield _init_variables_1648


class TestClass1648:
    def test_solution_0(self, init_variables_1648):
        assert init_variables_1648().max_profit([2, 5], 4) == 14

    def test_solution_1(self, init_variables_1648):
        assert init_variables_1648().max_profit([3, 5], 6) == 19

    def test_solution_2(self, init_variables_1648):
        assert init_variables_1648().max_profit([2, 8, 4, 10, 6], 20) == 110

    def test_solution_3(self, init_variables_1648):
        assert init_variables_1648().max_profit([1000000000], 1000000000) == 21
