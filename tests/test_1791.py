#!/usr/bin/env python

import pytest

"""
Test 1791. Find Center of Star Graph
"""


@pytest.fixture(scope="session")
def init_variables_1791():
    from src.leetcode_1791_find_center_of_star_graph import Solution

    solution = Solution()

    def _init_variables_1791():
        return solution

    yield _init_variables_1791


class TestClass1791:
    def test_solution_0(self, init_variables_1791):
        assert init_variables_1791().findCenter([[1, 2], [2, 3], [4, 2]]) == 2

    def test_solution_1(self, init_variables_1791):
        assert init_variables_1791().findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
