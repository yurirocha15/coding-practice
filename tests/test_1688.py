#!/usr/bin/env python

import pytest

"""
Test 1688. Count of Matches in Tournament
"""


@pytest.fixture(scope="session")
def init_variables_1688():
    from src.leetcode_1688_count_of_matches_in_tournament import Solution

    solution = Solution()

    def _init_variables_1688():
        return solution

    yield _init_variables_1688


class TestClass1688:
    def test_solution_0(self, init_variables_1688):
        assert init_variables_1688().numberOfMatches(7) == 6

    def test_solution_1(self, init_variables_1688):
        assert init_variables_1688().numberOfMatches(14) == 13
