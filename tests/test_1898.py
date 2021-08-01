#!/usr/bin/env python

import pytest

"""
Test 1898. Maximum Number of Removable Characters
"""


@pytest.fixture(scope="session")
def init_variables_1898():
    from src.leetcode_1898_maximum_number_of_removable_characters import Solution

    solution = Solution()

    def _init_variables_1898():
        return solution

    yield _init_variables_1898


class TestClass1898:
    def test_solution_0(self, init_variables_1898):
        assert init_variables_1898().maximumRemovals("abcacb", "ab", [3, 1, 0]) == 2

    def test_solution_1(self, init_variables_1898):
        assert (
            init_variables_1898().maximumRemovals(
                "abcbddddd", "abcd", [3, 2, 1, 4, 5, 6]
            )
            == 1
        )

    def test_solution_2(self, init_variables_1898):
        assert (
            init_variables_1898().maximumRemovals("abcab", "abc", [0, 1, 2, 3, 4]) == 0
        )
