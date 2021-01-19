#!/usr/bin/env python

import pytest

"""
Test 1675: minimize_deviation_in_array
"""


@pytest.fixture(scope="session")
def init_variables_1675():
    from src.heap_problems.minimize_deviation_in_array import Solution

    solution = Solution()

    def _init_variables_1675():
        return solution

    yield _init_variables_1675


class TestClass1675:
    def test_solution_0(self, init_variables_1675):
        assert init_variables_1675().minimum_deviation([1, 2, 3, 4]) == 1

    def test_solution_1(self, init_variables_1675):
        assert init_variables_1675().minimum_deviation([4, 1, 5, 20, 3]) == 3

    def test_solution_2(self, init_variables_1675):
        assert init_variables_1675().minimum_deviation([2, 10, 8]) == 3


"""
Test 347. Top K Frequent Elements
"""


@pytest.fixture(scope="session")
def init_variables_347():
    from src.heap_problems.top_k_frequent_elements import Solution

    solution = Solution()

    def _init_variables_347():
        return solution

    yield _init_variables_347


class TestClass347:
    def test_solution_0(self, init_variables_347):
        assert init_variables_347().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]

    def test_solution_1(self, init_variables_347):
        assert init_variables_347().topKFrequent([1], 1) == [1]
