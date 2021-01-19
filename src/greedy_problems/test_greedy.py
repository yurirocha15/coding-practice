#!/usr/bin/env python

import pytest

"""
Test 1688. Count of Matches in Tournament
"""


@pytest.fixture(scope="session")
def init_variables_1688():
    from src.greedy_problems.count_of_matches_in_tournament import Solution

    solution = Solution()

    def _init_variables_1688():
        return solution

    yield _init_variables_1688


class TestClass1688:
    def test_solution_0(self, init_variables_1688):
        assert init_variables_1688().number_of_matches(7) == 6

    def test_solution_1(self, init_variables_1688):
        assert init_variables_1688().number_of_matches(14) == 13


"""
Test 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
"""


@pytest.fixture(scope="session")
def init_variables_1689():
    from src.greedy_problems.partitioning_into_minimum_number_of_decibinary_numbers import Solution

    solution = Solution()

    def _init_variables_1689():
        return solution

    yield _init_variables_1689


class TestClass1689:
    def test_solution_0(self, init_variables_1689):
        assert init_variables_1689().min_partitions("32") == 3

    def test_solution_1(self, init_variables_1689):
        assert init_variables_1689().min_partitions("82734") == 8

    def test_solution_2(self, init_variables_1689):
        assert init_variables_1689().min_partitions("27346209830709182346") == 9


"""
Test 1722. Minimize Hamming Distance After Swap Operations
"""


@pytest.fixture(scope="session")
def init_variables_1722():
    from src.greedy_problems.minimize_hamming_distance_after_swap_operations import Solution

    solution = Solution()

    def _init_variables_1722():
        return solution

    yield _init_variables_1722


class TestClass1722:
    def test_solution_0(self, init_variables_1722):
        assert (
            init_variables_1722().minimumHammingDistance(
                source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]
            )
            == 1
        )

    def test_solution_1(self, init_variables_1722):
        assert (
            init_variables_1722().minimumHammingDistance(
                source=[1, 2, 3, 4], target=[1, 3, 2, 4], allowedSwaps=[]
            )
            == 2
        )

    def test_solution_2(self, init_variables_1722):
        assert (
            init_variables_1722().minimumHammingDistance(
                source=[5, 1, 2, 4, 3],
                target=[1, 5, 4, 2, 3],
                allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]],
            )
            == 0
        )
