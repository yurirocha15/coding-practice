#!/usr/bin/env python

import pytest

"""
Test 1822. Sign of the Product of an Array
"""


@pytest.fixture(scope="session")
def init_variables_1822():
    from src.leetcode_1822_sign_of_the_product_of_an_array import Solution

    solution = Solution()

    def _init_variables_1822():
        return solution

    yield _init_variables_1822


class TestClass1822:
    def test_solution_0(self, init_variables_1822):
        assert init_variables_1822().arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1

    def test_solution_1(self, init_variables_1822):
        assert init_variables_1822().arraySign([1, 5, 0, 2, -3]) == 0

    def test_solution_2(self, init_variables_1822):
        assert init_variables_1822().arraySign([-1, 1, -1, 1, -1]) == -1
