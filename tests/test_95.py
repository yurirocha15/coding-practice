#!/usr/bin/env python

from typing import List, Optional

import pytest

from src.leetcode_95_unique_binary_search_trees_ii import TreeNode

"""
Test 95. Unique Binary Search Trees II
"""


@pytest.fixture(scope="session")
def init_variables_95():
    from src.leetcode_95_unique_binary_search_trees_ii import Solution

    solution = Solution()

    def _init_variables_95():
        return solution

    yield _init_variables_95


@pytest.fixture(scope="session")
def convert_output_95():
    from collections import deque

    from src.leetcode_95_unique_binary_search_trees_ii import TreeNode

    def _convert_output_95(tl: List[TreeNode]):
        res = []
        for t in tl:
            dq = deque()
            dq.append(t)
            res.append([])
            while dq:
                cur: TreeNode = dq.popleft()
                if cur:
                    res[-1].append(cur.val)
                    if cur.left or cur.right:
                        dq.append(cur.left)
                        dq.append(cur.right)
                else:
                    res[-1].append(cur)
            for r in range(len(res[-1]) - 1, -1, -1):
                if res[-1][r]:
                    break
                del res[-1][r]
        return res

    yield _convert_output_95


class TestClass95:
    def test_solution_0(self, init_variables_95, convert_output_95):
        assert convert_output_95(init_variables_95().generateTrees(3)) == [
            [1, None, 2, None, 3],
            [1, None, 3, 2],
            [2, 1, 3],
            [3, 1, None, None, 2],
            [3, 2, None, 1],
        ]

    def test_solution_1(self, init_variables_95, convert_output_95):
        assert convert_output_95(init_variables_95().generateTrees(1)) == [[1]]
