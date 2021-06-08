#!/usr/bin/env python

import pytest

"""
Test 1659: maximize_grid_happiness
"""


@pytest.fixture(scope="session")
def init_variables_1659():
    from src.dp_problems.maximize_grid_happiness import Solution

    solution = Solution()

    def _init_variables_1659():
        return solution

    yield _init_variables_1659


class TestClass1659:
    def test_solution_0(self, init_variables_1659):
        assert init_variables_1659().get_max_grid_happiness(2, 3, 1, 2) == 240

    def test_solution_1(self, init_variables_1659):
        assert init_variables_1659().get_max_grid_happiness(3, 1, 2, 1) == 260

    def test_solution_2(self, init_variables_1659):
        assert init_variables_1659().get_max_grid_happiness(2, 2, 4, 0) == 240


"""
Test 1658: minimum_operations_to_reduce_x_to_zero
"""


@pytest.fixture(scope="session")
def init_variables_1658():
    from src.dp_problems.minimum_operations_to_reduce_x_to_zero import Solution

    solution = Solution()

    def _init_variables_1658():
        return solution

    yield _init_variables_1658


class TestClass1658:
    def test_solution_0(self, init_variables_1658):
        assert init_variables_1658().min_operations([1, 1, 4, 2, 3], 5) == 2

    def test_solution_1(self, init_variables_1658):
        assert init_variables_1658().min_operations([5, 6, 7, 8, 9], 4) == -1

    def test_solution_2(self, init_variables_1658):
        assert init_variables_1658().min_operations([3, 2, 20, 1, 1, 3], 10) == 5


"""
Test 1690. Stone Game VII
"""


@pytest.fixture(scope="session")
def init_variables_1690():
    from src.dp_problems.stone_game_vii import Solution

    solution = Solution()

    def _init_variables_1690():
        return solution

    yield _init_variables_1690


class TestClass1690:
    def test_solution_0(self, init_variables_1690):
        assert init_variables_1690().stone_game_VII([5, 3, 1, 4, 2]) == 6

    def test_solution_1(self, init_variables_1690):
        assert (
            init_variables_1690().stone_game_VII([7, 90, 5, 1, 100, 10, 10, 2]) == 122
        )


"""
Test 1728. Cat and Mouse II
"""


@pytest.fixture(scope="session")
def init_variables_1728():
    from src.dp_problems.cat_and_mouse_ii import Solution

    solution = Solution()

    def _init_variables_1728():
        return solution

    yield _init_variables_1728


class TestClass1728:
    def test_solution_0(self, init_variables_1728):
        assert init_variables_1728().can_mouse_win(
            grid=["####F", "#C...", "M...."], catJump=1, mouseJump=2
        )

    def test_solution_1(self, init_variables_1728):
        assert init_variables_1728().can_mouse_win(
            grid=["M.C...F"], catJump=1, mouseJump=4
        )

    def test_solution_2(self, init_variables_1728):
        assert not init_variables_1728().can_mouse_win(
            grid=["M.C...F"], catJump=1, mouseJump=3
        )

    def test_solution_3(self, init_variables_1728):
        assert not init_variables_1728().can_mouse_win(
            grid=["C...#", "...#F", "....#", "M...."], catJump=2, mouseJump=5
        )

    def test_solution_4(self, init_variables_1728):
        assert init_variables_1728().can_mouse_win(
            grid=[".M...", "..#..", "#..#.", "C#.#.", "...#F"], catJump=3, mouseJump=1
        )


"""
Test 1745. Palindrome Partitioning IV
"""


@pytest.fixture(scope="session")
def init_variables_1745():
    from src.dp_problems.palindrome_partitioning_iv import Solution

    solution = Solution()

    def _init_variables_1745():
        return solution

    yield _init_variables_1745


class TestClass1745:
    def test_solution_0(self, init_variables_1745):
        assert init_variables_1745().check_partitioning(s="abcbdd") is True

    def test_solution_1(self, init_variables_1745):
        assert init_variables_1745().check_partitioning(s="bcbddxy") is False


"""
Test 1770. Maximum Score from Performing Multiplication Operations
"""


@pytest.fixture(scope="session")
def init_variables_1770():
    from src.dp_problems.maximum_score_from_performing_multiplication_operations import Solution

    solution = Solution()

    def _init_variables_1770():
        return solution

    yield _init_variables_1770


class TestClass1770:
    def test_solution_0(self, init_variables_1770):
        assert (
            init_variables_1770().maximum_score(nums=[1, 2, 3], multipliers=[3, 2, 1])
            == 14
        )

    def test_solution_1(self, init_variables_1770):
        assert (
            init_variables_1770().maximum_score(
                nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]
            )
            == 102
        )


"""
Test 1771. Maximize Palindrome Length From Subsequences
"""


@pytest.fixture(scope="session")
def init_variables_1771():
    from src.dp_problems.maximize_palindrome_length_from_subsequences import Solution

    solution = Solution()

    def _init_variables_1771():
        return solution

    yield _init_variables_1771


class TestClass1771:
    def test_solution_0(self, init_variables_1771):
        assert init_variables_1771().longest_palindrome(word1="cacb", word2="cbba") == 5

    def test_solution_1(self, init_variables_1771):
        assert init_variables_1771().longest_palindrome(word1="ab", word2="ab") == 3

    def test_solution_2(self, init_variables_1771):
        assert init_variables_1771().longest_palindrome(word1="aa", word2="bb") == 0


"""
Test 1856. Maximum Subarray Min-Product
"""


@pytest.fixture(scope="session")
def init_variables_1856():
    from src.dp_problems.maximum_subarray_minproduct import Solution

    solution = Solution()

    def _init_variables_1856():
        return solution

    yield _init_variables_1856


class TestClass1856:
    def test_solution_0(self, init_variables_1856):
        assert init_variables_1856().max_sum_min_product(nums=[1, 2, 3, 2]) == 14

    def test_solution_1(self, init_variables_1856):
        assert init_variables_1856().max_sum_min_product(nums=[2, 3, 3, 1, 2]) == 18

    def test_solution_2(self, init_variables_1856):
        assert init_variables_1856().max_sum_min_product(nums=[3, 1, 5, 6, 4, 2]) == 60


"""
Test 1857. Largest Color Value in a Directed Graph
"""


@pytest.fixture(scope="session")
def init_variables_1857():
    from src.dp_problems.largest_color_value_in_a_directed_graph import Solution

    solution = Solution()

    def _init_variables_1857():
        return solution

    yield _init_variables_1857


class TestClass1857:
    def test_solution_0(self, init_variables_1857):
        assert (
            init_variables_1857().largest_path_value(
                colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]
            )
            == 3
        )

    def test_solution_1(self, init_variables_1857):
        assert (
            init_variables_1857().largest_path_value(colors="a", edges=[[0, 0]]) == -1
        )


"""
Test 1872. Stone Game VIII
"""


@pytest.fixture(scope="session")
def init_variables_1872():
    from src.dp_problems.stone_game_viii import Solution

    solution = Solution()

    def _init_variables_1872():
        return solution

    yield _init_variables_1872


class TestClass1872:
    def test_solution_0(self, init_variables_1872):
        assert init_variables_1872().stone_game_v_i_i_i(stones=[-1, 2, -3, 4, -5]) == 5

    def test_solution_1(self, init_variables_1872):
        assert (
            init_variables_1872().stone_game_v_i_i_i(stones=[7, -6, 5, 10, 5, -2, -6])
            == 13
        )

    def test_solution_2(self, init_variables_1872):
        assert init_variables_1872().stone_game_v_i_i_i(stones=[-10, -12]) == -22
