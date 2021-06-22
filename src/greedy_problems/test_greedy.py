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


"""
Test 1801. Number of Orders in the Backlog
"""


@pytest.fixture(scope="session")
def init_variables_1801():
    from src.greedy_problems.number_of_orders_in_the_backlog import Solution

    solution = Solution()

    def _init_variables_1801():
        return solution

    yield _init_variables_1801


class TestClass1801:
    def test_solution_0(self, init_variables_1801):
        assert (
            init_variables_1801().get_number_of_backlog_orders(
                orders=[[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
            )
            == 6
        )

    def test_solution_1(self, init_variables_1801):
        assert (
            init_variables_1801().get_number_of_backlog_orders(
                orders=[[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
            )
            == 999999984
        )


"""
Test 1802. Maximum Value at a Given Index in a Bounded Array
"""


@pytest.fixture(scope="session")
def init_variables_1802():
    from src.greedy_problems.maximum_value_at_a_given_index_in_a_bounded_array import Solution

    solution = Solution()

    def _init_variables_1802():
        return solution

    yield _init_variables_1802


class TestClass1802:
    def test_solution_0(self, init_variables_1802):
        assert init_variables_1802().max_value(n=4, index=2, maxSum=6) == 2

    def test_solution_1(self, init_variables_1802):
        assert init_variables_1802().max_value(n=6, index=1, maxSum=10) == 3


"""
Test 1808. Maximize Number of Nice Divisors
"""


@pytest.fixture(scope="session")
def init_variables_1808():
    from src.greedy_problems.maximize_number_of_nice_divisors import Solution

    solution = Solution()

    def _init_variables_1808():
        return solution

    yield _init_variables_1808


class TestClass1808:
    def test_solution_0(self, init_variables_1808):
        assert init_variables_1808().max_nice_divisors(primeFactors=5) == 6

    def test_solution_1(self, init_variables_1808):
        assert init_variables_1808().max_nice_divisors(primeFactors=8) == 18


"""
Test 1838. Frequency of the Most Frequent Element
"""


@pytest.fixture(scope="session")
def init_variables_1838():
    from src.greedy_problems.frequency_of_the_most_frequent_element import Solution

    solution = Solution()

    def _init_variables_1838():
        return solution

    yield _init_variables_1838


class TestClass1838:
    def test_solution_0(self, init_variables_1838):
        assert init_variables_1838().max_frequency(nums=[1, 2, 4], k=5) == 3

    def test_solution_1(self, init_variables_1838):
        assert init_variables_1838().max_frequency(nums=[1, 4, 8, 13], k=5) == 2

    def test_solution_2(self, init_variables_1838):
        assert init_variables_1838().max_frequency(nums=[3, 9, 6], k=2) == 1


"""
Test 1840. Maximum Building Height
"""


@pytest.fixture(scope="session")
def init_variables_1840():
    from src.greedy_problems.maximum_building_height import Solution

    solution = Solution()

    def _init_variables_1840():
        return solution

    yield _init_variables_1840


class TestClass1840:
    def test_solution_0(self, init_variables_1840):
        assert (
            init_variables_1840().max_building(n=5, restrictions=[[2, 1], [4, 1]]) == 2
        )

    def test_solution_1(self, init_variables_1840):
        assert init_variables_1840().max_building(n=6, restrictions=[]) == 5

    def test_solution_2(self, init_variables_1840):
        assert (
            init_variables_1840().max_building(
                n=10, restrictions=[[5, 3], [2, 5], [7, 4], [10, 3]]
            )
            == 5
        )


"""
Test 1855. Maximum Distance Between a Pair of Values
"""


@pytest.fixture(scope="session")
def init_variables_1855():
    from src.greedy_problems.maximum_distance_between_a_pair_of_values import Solution

    solution = Solution()

    def _init_variables_1855():
        return solution

    yield _init_variables_1855


class TestClass1855:
    def test_solution_0(self, init_variables_1855):
        assert (
            init_variables_1855().max_distance(
                nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]
            )
            == 2
        )

    def test_solution_1(self, init_variables_1855):
        assert (
            init_variables_1855().max_distance(nums1=[2, 2, 2], nums2=[10, 10, 1]) == 1
        )

    def test_solution_2(self, init_variables_1855):
        assert (
            init_variables_1855().max_distance(
                nums1=[30, 29, 19, 5], nums2=[25, 25, 25, 25, 25]
            )
            == 2
        )

    def test_solution_3(self, init_variables_1855):
        assert init_variables_1855().max_distance(nums1=[5, 4], nums2=[3, 2]) == 0


"""
Test 1871. Jump Game VII
"""


@pytest.fixture(scope="session")
def init_variables_1871():
    from src.greedy_problems.jump_game_vii import Solution

    solution = Solution()

    def _init_variables_1871():
        return solution

    yield _init_variables_1871


class TestClass1871:
    def test_solution_0(self, init_variables_1871):
        assert init_variables_1871().can_reach(s="011010", minJump=2, maxJump=3)

    def test_solution_1(self, init_variables_1871):
        assert not init_variables_1871().can_reach(s="01101110", minJump=2, maxJump=3)


"""
Test 1881. Maximum Value after Insertion
"""


@pytest.fixture(scope="session")
def init_variables_1881():
    from src.greedy_problems.maximum_value_after_insertion import Solution

    solution = Solution()

    def _init_variables_1881():
        return solution

    yield _init_variables_1881


class TestClass1881:
    def test_solution_0(self, init_variables_1881):
        assert init_variables_1881().max_value(n="99", x=9) == "999"

    def test_solution_1(self, init_variables_1881):
        assert init_variables_1881().max_value(n="-13", x=2) == "-123"


"""
Test 1887. Reduction Operations to Make the Array Elements Equal
"""


@pytest.fixture(scope="session")
def init_variables_1887():
    from src.greedy_problems.reduction_operations_to_make_the_array_elements_equal import Solution

    solution = Solution()

    def _init_variables_1887():
        return solution

    yield _init_variables_1887


class TestClass1887:
    def test_solution_0(self, init_variables_1887):
        assert init_variables_1887().reduction_operations(nums=[5, 1, 3]) == 3

    def test_solution_1(self, init_variables_1887):
        assert init_variables_1887().reduction_operations(nums=[1, 1, 1]) == 0

    def test_solution_2(self, init_variables_1887):
        assert init_variables_1887().reduction_operations(nums=[1, 1, 2, 2, 3]) == 4
