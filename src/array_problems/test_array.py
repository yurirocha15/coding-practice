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
