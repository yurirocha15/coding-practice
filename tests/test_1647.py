#!/usr/bin/env python

import pytest

"""
Test 1647. Minimum Deletions to Make Character Frequencies Unique
"""


@pytest.fixture(scope="session")
def init_variables_1647():
    from src.leetcode_1647_minimum_deletions_to_make_character_frequencies_unique import Solution

    solution = Solution()

    def _init_variables_1647():
        return solution

    yield _init_variables_1647


class TestClass1647:
    def test_solution_0(self, init_variables_1647):
        assert init_variables_1647().minDeletions("aab") == 0

    def test_solution_1(self, init_variables_1647):
        assert init_variables_1647().minDeletions("aaabbbcc") == 2

    def test_solution_2(self, init_variables_1647):
        assert init_variables_1647().minDeletions("ceabaacb") == 2
