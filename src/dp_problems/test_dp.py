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
