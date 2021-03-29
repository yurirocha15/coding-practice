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


"""
Test 1760. Minimum Limit of Balls in a Bag
"""


@pytest.fixture(scope="session")
def init_variables_1760():
    from src.heap_problems.minimum_limit_of_balls_in_a_bag import Solution

    solution = Solution()

    def _init_variables_1760():
        return solution

    yield _init_variables_1760


class TestClass1760:
    def test_solution_0(self, init_variables_1760):
        assert init_variables_1760().minimum_size(nums=[9], maxOperations=2) == 3

    def test_solution_1(self, init_variables_1760):
        assert (
            init_variables_1760().minimum_size(nums=[2, 4, 8, 2], maxOperations=4) == 2
        )

    def test_solution_2(self, init_variables_1760):
        assert init_variables_1760().minimum_size(nums=[7, 17], maxOperations=2) == 7


"""
Test 1792. Maximum Average Pass Ratio
"""


@pytest.fixture(scope="session")
def init_variables_1792():
    from src.heap_problems.maximum_average_pass_ratio import Solution

    solution = Solution()

    def _init_variables_1792():
        return solution

    yield _init_variables_1792


class TestClass1792:
    def test_solution_0(self, init_variables_1792):
        assert (
            init_variables_1792().max_average_ratio(
                classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2
            )
            - 0.78333
            < 10e-5
        )

    def test_solution_1(self, init_variables_1792):
        assert (
            init_variables_1792().max_average_ratio(
                classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4
            )
            - 0.53485
            < 10e-5
        )
