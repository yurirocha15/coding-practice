#!/usr/bin/env python

import pytest

"""
Test 1721. Swapping Nodes in a Linked List
"""


@pytest.fixture(scope="session")
def init_variables_1721():
    from src.list_problems.swapping_nodes_in_a_linked_list import ListNode, Solution

    solution = Solution()

    def _init_variables_1721():
        head = None
        input = [1, 2, 3, 4, 5]
        for n in input[::-1]:
            head = ListNode(n, head)
        return solution, head

    yield _init_variables_1721


class TestClass1721:
    def test_solution_0(self, init_variables_1721):
        assert (
            init_variables_1721()[0].swapNodes(init_variables_1721()[1], 2).next.val
            == 4
        )
