#!/usr/bin/env python

import pytest

"""
Test 1720. Decode XORed Array
"""


@pytest.fixture(scope="session")
def init_variables_1720():
    from src.leetcode_1720_decode_xored_array import Solution

    solution = Solution()

    def _init_variables_1720():
        return solution

    yield _init_variables_1720


class TestClass1720:
    def test_solution_0(self, init_variables_1720):
        assert init_variables_1720().decode([1, 2, 3], 1) == [1, 0, 2, 1]

    def test_solution_1(self, init_variables_1720):
        assert init_variables_1720().decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
