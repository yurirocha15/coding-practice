#!/usr/bin/env python

import pytest

"""
Test 1822. Sign of the Product of an Array
"""


@pytest.fixture(scope="session")
def init_variables_1822():
    from src.math_problems.sign_of_the_product_of_an_array import Solution

    solution = Solution()

    def _init_variables_1822():
        return solution

    yield _init_variables_1822


class TestClass1822:
    def test_solution_0(self, init_variables_1822):
        assert init_variables_1822().array_sign(nums=[-1, -2, -3, -4, 3, 2, 1]) == 1

    def test_solution_1(self, init_variables_1822):
        assert init_variables_1822().array_sign(nums=[1, 5, 0, 2, -3]) == 0

    def test_solution_2(self, init_variables_1822):
        assert init_variables_1822().array_sign(nums=[-1, 1, -1, 1, -1]) == -1


"""
Test 1835. Find XOR Sum of All Pairs Bitwise AND
"""


@pytest.fixture(scope="session")
def init_variables_1835():
    from src.math_problems.find_xor_sum_of_all_pairs_bitwise_and import Solution

    solution = Solution()

    def _init_variables_1835():
        return solution

    yield _init_variables_1835


class TestClass1835:
    def test_solution_0(self, init_variables_1835):
        assert init_variables_1835().get_x_o_r_sum(arr1=[1, 2, 3], arr2=[6, 5]) == 0

    def test_solution_1(self, init_variables_1835):
        assert init_variables_1835().get_x_o_r_sum(arr1=[12], arr2=[4]) == 4


"""
Test 1837. Sum of Digits in Base K
"""


@pytest.fixture(scope="session")
def init_variables_1837():
    from src.math_problems.sum_of_digits_in_base_k import Solution

    solution = Solution()

    def _init_variables_1837():
        return solution

    yield _init_variables_1837


class TestClass1837:
    def test_solution_0(self, init_variables_1837):
        assert init_variables_1837().sum_base(n=34, k=6) == 9

    def test_solution_1(self, init_variables_1837):
        assert init_variables_1837().sum_base(n=10, k=10) == 1
