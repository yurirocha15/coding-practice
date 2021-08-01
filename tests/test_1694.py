#!/usr/bin/env python

import pytest

"""
Test 1694. Reformat Phone Number
"""


@pytest.fixture(scope="session")
def init_variables_1694():
    from src.leetcode_1694_reformat_phone_number import Solution

    solution = Solution()

    def _init_variables_1694():
        return solution

    yield _init_variables_1694


class TestClass1694:
    def test_solution_0(self, init_variables_1694):
        assert init_variables_1694().reformatNumber("1-23-45 6") == "123-456"

    def test_solution_1(self, init_variables_1694):
        assert init_variables_1694().reformatNumber("123 4-567") == "123-45-67"

    def test_solution_2(self, init_variables_1694):
        assert init_variables_1694().reformatNumber("123 4-5678") == "123-456-78"

    def test_solution_3(self, init_variables_1694):
        assert init_variables_1694().reformatNumber("12") == "12"

    def test_solution_4(self, init_variables_1694):
        assert (
            init_variables_1694().reformatNumber("--17-5 229 35-39475 ")
            == "175-229-353-94-75"
        )
