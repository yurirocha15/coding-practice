#!/usr/bin/env python

import pytest

"""
Test 96. Unique Binary Search Trees
"""


@pytest.fixture(scope="session")
def init_variables_96():
    from src.leetcode_96_unique_binary_search_trees import Solution

    solution = Solution()

    def _init_variables_96():
        return solution

    yield _init_variables_96


class TestClass96:
    def test_solution_0(self, init_variables_96):
        assert init_variables_96().numTrees(3) == 5

    def test_solution_1(self, init_variables_96):
        assert init_variables_96().numTrees(1) == 1
