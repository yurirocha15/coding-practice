#!/usr/bin/env python

import pytest

"""
Test 1761. Minimum Degree of a Connected Trio in a Graph
"""


@pytest.fixture(scope="session")
def init_variables_1761():
    from src.leetcode_1761_minimum_degree_of_a_connected_trio_in_a_graph import Solution

    solution = Solution()

    def _init_variables_1761():
        return solution

    yield _init_variables_1761


class TestClass1761:
    def test_solution_0(self, init_variables_1761):
        assert (
            init_variables_1761().minTrioDegree(
                6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
            )
            == 3
        )

    def test_solution_1(self, init_variables_1761):
        assert (
            init_variables_1761().minTrioDegree(
                7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]
            )
            == 0
        )
