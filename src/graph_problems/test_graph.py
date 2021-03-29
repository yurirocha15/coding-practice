#!/usr/bin/env python

import pytest

"""
Test 1761. Minimum Degree of a Connected Trio in a Graph
"""


@pytest.fixture(scope="session")
def init_variables_1761():
    from src.graph_problems.minimum_degree_of_a_connected_trio_in_a_graph import Solution

    solution = Solution()

    def _init_variables_1761():
        return solution

    yield _init_variables_1761


class TestClass1761:
    def test_solution_0(self, init_variables_1761):
        assert (
            init_variables_1761().min_trio_degree(
                n=6, edges=[[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
            )
            == 3
        )

    def test_solution_1(self, init_variables_1761):
        assert (
            init_variables_1761().min_trio_degree(
                n=7,
                edges=[[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]],
            )
            == 0
        )


"""
Test 1791. Find Center of Star Graph
"""


@pytest.fixture(scope="session")
def init_variables_1791():
    from src.graph_problems.find_center_of_star_graph import Solution

    solution = Solution()

    def _init_variables_1791():
        return solution

    yield _init_variables_1791


class TestClass1791:
    def test_solution_0(self, init_variables_1791):
        assert init_variables_1791().find_center(edges=[[1, 2], [2, 3], [4, 2]]) == 2

    def test_solution_1(self, init_variables_1791):
        assert (
            init_variables_1791().find_center(edges=[[1, 2], [5, 1], [1, 3], [1, 4]])
            == 1
        )
