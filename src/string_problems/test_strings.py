#!/usr/bin/env python

import pytest

"""
Test 1662: check_if_two_string_arrays_are_equivalent
"""


@pytest.fixture(scope="session")
def init_variables_1662():
    from src.string_problems.check_if_two_string_arrays_are_equivalent import Solution

    solution = Solution()

    def _init_variables_1662():
        return solution

    yield _init_variables_1662


class TestClass1662:
    def test_solution_0(self, init_variables_1662):
        assert init_variables_1662().array_strings_are_equal(["ab", "c"], ["a", "bc"])

    def test_solution_1(self, init_variables_1662):
        assert not init_variables_1662().array_strings_are_equal(
            ["a", "cb"], ["ab", "c"]
        )

    def test_solution_2(self, init_variables_1662):
        assert init_variables_1662().array_strings_are_equal(
            ["abc", "d", "defg"], ["abcddefg"]
        )


"""
Test 1657: determine_if_two_strings_are_close
"""


@pytest.fixture(scope="session")
def init_variables_1657():
    from src.string_problems.determine_if_two_strings_are_close import Solution

    solution = Solution()

    def _init_variables_1657():
        return solution

    yield _init_variables_1657


class TestClass1657:
    def test_solution_0(self, init_variables_1657):
        assert init_variables_1657().close_strings("abc", "bca")

    def test_solution_1(self, init_variables_1657):
        assert not init_variables_1657().close_strings("a", "aa")

    def test_solution_2(self, init_variables_1657):
        assert init_variables_1657().close_strings("cabbba", "abbccc")

    def test_solution_3(self, init_variables_1657):
        assert not init_variables_1657().close_strings("cabbba", "aabbss")


"""
Test 1663: smallest_string_with_a_given_numeric_value
"""


@pytest.fixture(scope="session")
def init_variables_1663():
    from src.string_problems.smallest_string_with_a_given_numeric_value import Solution

    solution = Solution()

    def _init_variables_1663():
        return solution

    yield _init_variables_1663


class TestClass1663:
    def test_solution_0(self, init_variables_1663):
        assert init_variables_1663().get_smallest_string(3, 27) == "aay"

    def test_solution_1(self, init_variables_1663):
        assert init_variables_1663().get_smallest_string(5, 73) == "aaszz"


"""
Test 1694. Reformat Phone Number
"""


@pytest.fixture(scope="session")
def init_variables_1694():
    from src.string_problems.reformat_phone_number import Solution

    solution = Solution()

    def _init_variables_1694():
        return solution

    yield _init_variables_1694


class TestClass1694:
    def test_solution_0(self, init_variables_1694):
        assert init_variables_1694().reformat_number("1-23-45 6") == "123-456"

    def test_solution_1(self, init_variables_1694):
        assert init_variables_1694().reformat_number("123 4-567") == "123-45-67"

    def test_solution_2(self, init_variables_1694):
        assert init_variables_1694().reformat_number("123 4-5678") == "123-456-78"

    def test_solution_3(self, init_variables_1694):
        assert init_variables_1694().reformat_number("12") == "12"

    def test_solution_4(self, init_variables_1694):
        assert (
            init_variables_1694().reformat_number("--17-5 229 35-39475 ")
            == "175-229-353-94-75"
        )
