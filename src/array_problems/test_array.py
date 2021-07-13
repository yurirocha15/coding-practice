#!/usr/bin/env python

import pytest

"""
Test 1656: design_an_ordered_stream
"""


@pytest.fixture(scope="session")
def init_variables_1656():
    from src.array_problems.design_an_ordered_stream import OrderedStream

    ordered_stream = OrderedStream(5)

    def _init_variables_1656():
        return ordered_stream

    yield _init_variables_1656


class TestClass1656:
    def test_solution_0(self, init_variables_1656):
        assert not init_variables_1656().insert(3, "ccccc")

    def test_solution_1(self, init_variables_1656):
        assert init_variables_1656().insert(1, "aaaaa") == ["aaaaa"]

    def test_solution_2(self, init_variables_1656):
        assert init_variables_1656().insert(2, "bbbbb") == ["bbbbb", "ccccc"]

    def test_solution_3(self, init_variables_1656):
        assert not init_variables_1656().insert(5, "eeeee")

    def test_solution_4(self, init_variables_1656):
        assert init_variables_1656().insert(4, "ddddd") == ["ddddd", "eeeee"]


"""
Test 1646: get_maximum_in_generated_array
"""


@pytest.fixture(scope="session")
def init_variables_1646():
    from src.array_problems.get_maximum_in_generated_array import Solution

    solution = Solution()

    def _init_variables_1646():
        return solution

    yield _init_variables_1646


class TestClass1646:
    def test_solution_0(self, init_variables_1646):
        assert init_variables_1646().get_maximum_generated(7) == 3

    def test_solution_1(self, init_variables_1646):
        assert init_variables_1646().get_maximum_generated(2) == 1

    def test_solution_2(self, init_variables_1646):
        assert init_variables_1646().get_maximum_generated(3) == 2


"""
Test 1672: richest_costumer_wealth
"""


@pytest.fixture(scope="session")
def init_variables_1672():
    from src.array_problems.richest_costumer_wealth import Solution

    solution = Solution()

    def _init_variables_1672():
        return solution

    yield _init_variables_1672


class TestClass1672:
    def test_solution_0(self, init_variables_1672):
        assert init_variables_1672().maximum_wealth([[1, 2, 3], [3, 2, 1]]) == 6

    def test_solution_1(self, init_variables_1672):
        assert init_variables_1672().maximum_wealth([[1, 5], [7, 3], [3, 5]]) == 10

    def test_solution_2(self, init_variables_1672):
        assert (
            init_variables_1672().maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
            == 17
        )


"""
Test 1674: minimum_moves_to_make_array_complementary
"""


@pytest.fixture(scope="session")
def init_variables_1674():
    from src.array_problems.minimum_moves_to_make_array_complementary import Solution

    solution = Solution()

    def _init_variables_1674():
        return solution

    yield _init_variables_1674


class TestClass1674:
    def test_solution_0(self, init_variables_1674):
        assert init_variables_1674().min_moves([1, 2, 4, 3], 4) == 1

    def test_solution_1(self, init_variables_1674):
        assert init_variables_1674().min_moves([1, 2, 2, 1], 2) == 2

    def test_solution_2(self, init_variables_1674):
        assert init_variables_1674().min_moves([1, 2, 1, 2], 2) == 0


"""
Test 1695. Maximum Erasure Value
"""


@pytest.fixture(scope="session")
def init_variables_1695():
    from src.array_problems.maximum_array_erase_value import Solution

    solution = Solution()

    def _init_variables_1695():
        return solution

    yield _init_variables_1695


class TestClass1695:
    def test_solution_0(self, init_variables_1695):
        assert init_variables_1695().maximum_unique_subarray([4, 2, 4, 5, 6]) == 17

    def test_solution_1(self, init_variables_1695):
        assert (
            init_variables_1695().maximum_unique_subarray([5, 2, 1, 2, 5, 2, 1, 2, 5])
            == 8
        )


"""
Test 1744. Can You Eat Your Favorite Candy on Your Favorite Day?
"""


@pytest.fixture(scope="session")
def init_variables_1744():
    from src.array_problems.can_you_eat_your_favorite_candy_on_your_favorite_day import Solution

    solution = Solution()

    def _init_variables_1744():
        return solution

    yield _init_variables_1744


class TestClass1744:
    def test_solution_0(self, init_variables_1744):
        assert init_variables_1744().can_eat(
            [7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
        ) == [True, False, True]


"""
Test 1742. Maximum Number of Balls in a Box
"""


@pytest.fixture(scope="session")
def init_variables_1742():
    from src.array_problems.maximum_number_of_balls_in_a_box import Solution

    solution = Solution()

    def _init_variables_1742():
        return solution

    yield _init_variables_1742


class TestClass1742:
    def test_solution_0(self, init_variables_1742):
        assert init_variables_1742().count_balls(lowLimit=1, highLimit=10) == 2

    def test_solution_1(self, init_variables_1742):
        assert init_variables_1742().count_balls(lowLimit=5, highLimit=15) == 2

    def test_solution_2(self, init_variables_1742):
        assert init_variables_1742().count_balls(lowLimit=19, highLimit=28) == 2


"""
Test 1769. Minimum Number of Operations to Move All Balls to Each Box
"""


@pytest.fixture(scope="session")
def init_variables_1769():
    from src.array_problems.minimum_number_of_operations_to_move_all_balls_to_each_box import Solution

    solution = Solution()

    def _init_variables_1769():
        return solution

    yield _init_variables_1769


class TestClass1769:
    def test_solution_0(self, init_variables_1769):
        assert init_variables_1769().min_operations(boxes="110") == [1, 1, 3]

    def test_solution_1(self, init_variables_1769):
        assert init_variables_1769().min_operations(boxes="001011") == [
            11,
            8,
            5,
            4,
            3,
            4,
        ]


"""
Test 1800. Maximum Ascending Subarray Sum
"""


@pytest.fixture(scope="session")
def init_variables_1800():
    from src.array_problems.maximum_ascending_subarray_sum import Solution

    solution = Solution()

    def _init_variables_1800():
        return solution

    yield _init_variables_1800


class TestClass1800:
    def test_solution_0(self, init_variables_1800):
        assert (
            init_variables_1800().max_ascending_sum(nums=[10, 20, 30, 5, 10, 50]) == 65
        )

    def test_solution_1(self, init_variables_1800):
        assert init_variables_1800().max_ascending_sum(nums=[10, 20, 30, 40, 50]) == 150

    def test_solution_2(self, init_variables_1800):
        assert (
            init_variables_1800().max_ascending_sum(nums=[12, 17, 15, 13, 10, 11, 12])
            == 33
        )

    def test_solution_3(self, init_variables_1800):
        assert init_variables_1800().max_ascending_sum(nums=[100, 10, 1]) == 100


"""
Test 1806. Minimum Number of Operations to Reinitialize a Permutation
"""


@pytest.fixture(scope="session")
def init_variables_1806():
    from src.array_problems.minimum_number_of_operations_to_reinitialize_a_permutation import Solution

    solution = Solution()

    def _init_variables_1806():
        return solution

    yield _init_variables_1806


class TestClass1806:
    def test_solution_0(self, init_variables_1806):
        assert init_variables_1806().reinitialize_permutation(n=2) == 1

    def test_solution_1(self, init_variables_1806):
        assert init_variables_1806().reinitialize_permutation(n=4) == 2

    def test_solution_2(self, init_variables_1806):
        assert init_variables_1806().reinitialize_permutation(n=6) == 4


"""
Test 1823. Find the Winner of the Circular Game
"""


@pytest.fixture(scope="session")
def init_variables_1823():
    from src.array_problems.find_the_winner_of_the_circular_game import Solution

    solution = Solution()

    def _init_variables_1823():
        return solution

    yield _init_variables_1823


class TestClass1823:
    def test_solution_0(self, init_variables_1823):
        assert init_variables_1823().find_the_winner(n=5, k=2) == 3

    def test_solution_1(self, init_variables_1823):
        assert init_variables_1823().find_the_winner(n=6, k=5) == 1


"""
Test 1833. Maximum Ice Cream Bars
"""


@pytest.fixture(scope="session")
def init_variables_1833():
    from src.array_problems.maximum_ice_cream_bars import Solution

    solution = Solution()

    def _init_variables_1833():
        return solution

    yield _init_variables_1833


class TestClass1833:
    def test_solution_0(self, init_variables_1833):
        assert init_variables_1833().max_ice_cream(costs=[1, 3, 2, 4, 1], coins=7) == 4

    def test_solution_1(self, init_variables_1833):
        assert (
            init_variables_1833().max_ice_cream(costs=[10, 6, 8, 7, 7, 8], coins=5) == 0
        )

    def test_solution_2(self, init_variables_1833):
        assert (
            init_variables_1833().max_ice_cream(costs=[1, 6, 3, 1, 2, 5], coins=20) == 6
        )


"""
Test 1854. Maximum Population Year
"""


@pytest.fixture(scope="session")
def init_variables_1854():
    from src.array_problems.maximum_population_year import Solution

    solution = Solution()

    def _init_variables_1854():
        return solution

    yield _init_variables_1854


class TestClass1854:
    def test_solution_0(self, init_variables_1854):
        assert (
            init_variables_1854().maximum_population(logs=[[1993, 1999], [2000, 2010]])
            == 1993
        )

    def test_solution_1(self, init_variables_1854):
        assert (
            init_variables_1854().maximum_population(
                logs=[[1950, 1961], [1960, 1971], [1970, 1981]]
            )
            == 1960
        )


"""
Test 1869. Longer Contiguous Segments of Ones than Zeros
"""


@pytest.fixture(scope="session")
def init_variables_1869():
    from src.array_problems.longer_contiguous_segments_of_ones_than_zeros import Solution

    solution = Solution()

    def _init_variables_1869():
        return solution

    yield _init_variables_1869


class TestClass1869:
    def test_solution_0(self, init_variables_1869):
        assert init_variables_1869().check_zero_ones(s="1101")

    def test_solution_1(self, init_variables_1869):
        assert not init_variables_1869().check_zero_ones(s="111000")

    def test_solution_2(self, init_variables_1869):
        assert not init_variables_1869().check_zero_ones(s="110100010")


"""
Test 1886. Determine Whether Matrix Can Be Obtained By Rotation
"""


@pytest.fixture(scope="session")
def init_variables_1886():
    from src.array_problems.determine_whether_matrix_can_be_obtained_by_rotation import Solution

    solution = Solution()

    def _init_variables_1886():
        return solution

    yield _init_variables_1886


class TestClass1886:
    def test_solution_0(self, init_variables_1886):
        assert init_variables_1886().find_rotation(
            mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]
        )

    def test_solution_1(self, init_variables_1886):
        assert not init_variables_1886().find_rotation(
            mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]
        )

    def test_solution_2(self, init_variables_1886):
        assert init_variables_1886().find_rotation(
            mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]],
        )


"""
Test 1898. Maximum Number of Removable Characters
"""


@pytest.fixture(scope="session")
def init_variables_1898():
    from src.array_problems.maximum_number_of_removable_characters import Solution

    solution = Solution()

    def _init_variables_1898():
        return solution

    yield _init_variables_1898


class TestClass1898:
    def test_solution_0(self, init_variables_1898):
        assert (
            init_variables_1898().maximum_removals(
                s="abcacb", p="ab", removable=[3, 1, 0]
            )
            == 2
        )

    def test_solution_1(self, init_variables_1898):
        assert (
            init_variables_1898().maximum_removals(
                s="abcbddddd", p="abcd", removable=[3, 2, 1, 4, 5, 6]
            )
            == 1
        )

    def test_solution_2(self, init_variables_1898):
        assert (
            init_variables_1898().maximum_removals(
                s="abcab", p="abc", removable=[0, 1, 2, 3, 4]
            )
            == 0
        )


"""
Test 1899. Merge Triplets to Form Target Triplet
"""


@pytest.fixture(scope="session")
def init_variables_1899():
    from src.array_problems.merge_triplets_to_form_target_triplet import Solution

    solution = Solution()

    def _init_variables_1899():
        return solution

    yield _init_variables_1899


class TestClass1899:
    def test_solution_0(self, init_variables_1899):
        assert init_variables_1899().merge_triplets(
            triplets=[[2, 5, 3], [1, 8, 4], [1, 7, 5]], target=[2, 7, 5]
        )

    def test_solution_1(self, init_variables_1899):
        assert init_variables_1899().merge_triplets(
            triplets=[[1, 3, 4], [2, 5, 8]], target=[2, 5, 8]
        )

    def test_solution_2(self, init_variables_1899):
        assert init_variables_1899().merge_triplets(
            triplets=[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target=[5, 5, 5]
        )

    def test_solution_3(self, init_variables_1899):
        assert not init_variables_1899().merge_triplets(
            triplets=[[3, 4, 5], [4, 5, 6]], target=[3, 2, 5]
        )


"""
Test 1914. Cyclically Rotating a Grid
"""


@pytest.fixture(scope="session")
def init_variables_1914():
    from src.array_problems.cyclically_rotating_a_grid import Solution

    solution = Solution()

    def _init_variables_1914():
        return solution

    yield _init_variables_1914


class TestClass1914:
    def test_solution_0(self, init_variables_1914):
        assert init_variables_1914().rotate_grid(grid=[[40, 10], [30, 20]], k=1) == [
            [10, 20],
            [40, 30],
        ]

    def test_solution_1(self, init_variables_1914):
        assert init_variables_1914().rotate_grid(
            grid=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], k=2
        ) == [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]]
