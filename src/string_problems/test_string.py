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


"""
Test 1736. Latest Time by Replacing Hidden Digits
"""


@pytest.fixture(scope="session")
def init_variables_1736():
    from src.string_problems.latest_time_by_replacing_hidden_digits import Solution

    solution = Solution()

    def _init_variables_1736():
        return solution

    yield _init_variables_1736


class TestClass1736:
    def test_solution_0(self, init_variables_1736):
        assert init_variables_1736().maximum_time("2?:?0") == "23:50"

    def test_solution_1(self, init_variables_1736):
        assert init_variables_1736().maximum_time("0?:3?") == "09:39"

    def test_solution_2(self, init_variables_1736):
        assert init_variables_1736().maximum_time("1?:22") == "19:22"


"""
Test 1737. Change Minimum Characters to Satisfy One of Three Conditions
"""


@pytest.fixture(scope="session")
def init_variables_1737():
    from src.string_problems.change_minimum_characters_to_satisfy_one_of_three_conditions import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1737():
        return solution

    yield _init_variables_1737


class TestClass1737:
    def test_solution_0(self, init_variables_1737):
        assert init_variables_1737().min_characters(a="aba", b="caa") == 2

    def test_solution_1(self, init_variables_1737):
        assert init_variables_1737().min_characters(a="dabadd", b="cda") == 3


"""
Test 1759. Count Number of Homogenous Substrings
"""


@pytest.fixture(scope="session")
def init_variables_1759():
    from src.string_problems.count_number_of_homogenous_substrings import Solution

    solution = Solution()

    def _init_variables_1759():
        return solution

    yield _init_variables_1759


class TestClass1759:
    def test_solution_0(self, init_variables_1759):
        assert init_variables_1759().count_homogenous(s="abbcccaa") == 13

    def test_solution_1(self, init_variables_1759):
        assert init_variables_1759().count_homogenous(s="xy") == 2

    def test_solution_2(self, init_variables_1759):
        assert init_variables_1759().count_homogenous(s="zzzzz") == 15
