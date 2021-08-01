#!/usr/bin/env python

from typing import List

import pytest

"""
Test 1721. Swapping Nodes in a Linked List
"""
from src.leetcode_1721_swapping_nodes_in_a_linked_list import ListNode


@pytest.fixture(scope="session")
def init_variables_1721():
    from src.leetcode_1721_swapping_nodes_in_a_linked_list import Solution

    solution = Solution()

    def _init_variables_1721():
        return solution

    yield _init_variables_1721


def build_list(nums: List[int]) -> ListNode:
    head = None
    for n in reversed(nums):
        head = ListNode(n, head)
    return head


def tear_list(ln: ListNode) -> List[int]:
    ret = []
    while ln:
        ret.append(ln.val)
        ln = ln.next
    return ret


class TestClass1721:
    def test_solution_0(self, init_variables_1721):
        assert tear_list(
            init_variables_1721().swapNodes(build_list([1, 2, 3, 4, 5]), 2)
        ) == [1, 4, 3, 2, 5]

    def test_solution_1(self, init_variables_1721):
        assert tear_list(
            init_variables_1721().swapNodes(
                build_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5
            )
        ) == [
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
        assert tear_list(init_variables_1721().swapNodes(build_list([1]), 1)) == [1]

    def test_solution_3(self, init_variables_1721):
        assert tear_list(init_variables_1721().swapNodes(build_list([1, 2]), 1)) == [
            2,
            1,
        ]

    def test_solution_4(self, init_variables_1721):
        assert tear_list(init_variables_1721().swapNodes(build_list([1, 2, 3]), 2)) == [
            1,
            2,
            3,
        ]
