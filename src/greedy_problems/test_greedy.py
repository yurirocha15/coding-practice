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
            init_variables_1722().minimum_hamming_distance(
                source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]
            )
            == 1
        )

    def test_solution_1(self, init_variables_1722):
        assert (
            init_variables_1722().minimum_hamming_distance(
                source=[1, 2, 3, 4], target=[1, 3, 2, 4], allowedSwaps=[]
            )
            == 2
        )

    def test_solution_2(self, init_variables_1722):
        assert (
            init_variables_1722().minimum_hamming_distance(
                source=[5, 1, 2, 4, 3],
                target=[1, 5, 4, 2, 3],
                allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]],
            )
            == 0
        )


"""
Test 1723. Find Minimum Time to Finish All Jobs
"""


@pytest.fixture(scope="session")
def init_variables_1723():
    from src.greedy_problems.find_minimum_time_to_finish_all_jobs import Solution

    solution = Solution()

    def _init_variables_1723():
        return solution

    yield _init_variables_1723


class TestClass1723:
    def test_solution_0(self, init_variables_1723):
        assert init_variables_1723().minimum_time_required(jobs=[3, 2, 3], k=3) == 3

    def test_solution_1(self, init_variables_1723):
        assert (
            init_variables_1723().minimum_time_required(jobs=[1, 2, 4, 7, 8], k=2) == 11
        )


"""
Test 1739. Building Boxes
"""


@pytest.fixture(scope="session")
def init_variables_1739():
    from src.greedy_problems.building_boxes import Solution

    solution = Solution()

    def _init_variables_1739():
        return solution

    yield _init_variables_1739


class TestClass1739:
    def test_solution_0(self, init_variables_1739):
        assert init_variables_1739().minimum_boxes(3) == 3

    def test_solution_1(self, init_variables_1739):
        assert init_variables_1739().minimum_boxes(4) == 3

    def test_solution_2(self, init_variables_1739):
        assert init_variables_1739().minimum_boxes(10) == 6


"""
Test 1743. Restore the Array From Adjacent Pairs
"""


@pytest.fixture(scope="session")
def init_variables_1743():
    from src.greedy_problems.restore_the_array_from_adjacent_pairs import Solution

    solution = Solution()

    def _init_variables_1743():
        return solution

    yield _init_variables_1743


class TestClass1743:
    def test_solution_0(self, init_variables_1743):
        assert init_variables_1743().restore_array(
            adjacentPairs=[[2, 1], [3, 4], [3, 2]]
        ) == [1, 2, 3, 4]

    def test_solution_1(self, init_variables_1743):
        assert init_variables_1743().restore_array(
            adjacentPairs=[[4, -2], [1, 4], [-3, 1]]
        ) == [-2, 4, 1, -3]

    def test_solution_2(self, init_variables_1743):
        assert init_variables_1743().restore_array(
            adjacentPairs=[[100000, -100000]]
        ) == [100000, -100000]


"""
Test 1758. Minimum Changes To Make Alternating Binary String
"""


@pytest.fixture(scope="session")
def init_variables_1758():
    from src.greedy_problems.minimum_changes_to_make_alternating_binary_string import Solution

    solution = Solution()

    def _init_variables_1758():
        return solution

    yield _init_variables_1758


class TestClass1758:
    def test_solution_0(self, init_variables_1758):
        assert init_variables_1758().min_operations(s="0100") == 1

    def test_solution_1(self, init_variables_1758):
        assert init_variables_1758().min_operations(s="10") == 0

    def test_solution_2(self, init_variables_1758):
        assert init_variables_1758().min_operations(s="1111") == 2


"""
Test 1784. Check if Binary String Has at Most One Segment of Ones
"""


@pytest.fixture(scope="session")
def init_variables_1784():
    from src.greedy_problems.check_if_binary_string_has_at_most_one_segment_of_ones import Solution

    solution = Solution()

    def _init_variables_1784():
        return solution

    yield _init_variables_1784


class TestClass1784:
    def test_solution_0(self, init_variables_1784):
        assert not init_variables_1784().check_ones_segment(s="1001")

    def test_solution_1(self, init_variables_1784):
        assert init_variables_1784().check_ones_segment(s="110")


"""
Test 1793. Maximum Score of a Good Subarray
"""


@pytest.fixture(scope="session")
def init_variables_1793():
    from src.greedy_problems.maximum_score_of_a_good_subarray import Solution

    solution = Solution()

    def _init_variables_1793():
        return solution

    yield _init_variables_1793


class TestClass1793:
    def test_solution_0(self, init_variables_1793):
        assert init_variables_1793().maximum_score(nums=[1, 4, 3, 7, 4, 5], k=3) == 15

    def test_solution_1(self, init_variables_1793):
        assert (
            init_variables_1793().maximum_score(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0)
            == 20
        )
