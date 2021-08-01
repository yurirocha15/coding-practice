#!/usr/bin/env python

import pytest

"""
Test 1721. Swapping Nodes in a Linked List
"""


@pytest.fixture(scope="session")
def init_variables_1721():
    from src.leetcode_1721_swapping_nodes_in_a_linked_list import Solution

    solution = Solution()

    def _init_variables_1721():
        return solution

    yield _init_variables_1721


class TestClass1721:
    def test_solution_0(self, init_variables_1721):
        assert init_variables_1721().swapNodes([1, 2, 3, 4, 5], 2) == [1, 4, 3, 2, 5]

    def test_solution_1(self, init_variables_1721):
        assert init_variables_1721().swapNodes([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5) == [
            7,
            9,
            6,
            6,
            8,
            7,
            3,
            0,
            9,
            5,
        ]

    def test_solution_2(self, init_variables_1721):
        assert init_variables_1721().swapNodes([1], 1) == [1]

    def test_solution_3(self, init_variables_1721):
        assert init_variables_1721().swapNodes([1, 2], 1) == [2, 1]

    def test_solution_4(self, init_variables_1721):
        assert init_variables_1721().swapNodes([1, 2, 3], 2) == [1, 2, 3]
