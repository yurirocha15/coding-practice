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


"""
Test 1870. Minimum Speed to Arrive on Time
"""


@pytest.fixture(scope="session")
def init_variables_1870():
    from src.math_problems.minimum_speed_to_arrive_on_time import Solution

    solution = Solution()

    def _init_variables_1870():
        return solution

    yield _init_variables_1870


class TestClass1870:
    def test_solution_0(self, init_variables_1870):
        assert init_variables_1870().min_speed_on_time(dist=[1, 3, 2], hour=6) == 1

    def test_solution_1(self, init_variables_1870):
        assert init_variables_1870().min_speed_on_time(dist=[1, 3, 2], hour=2.7) == 3

    def test_solution_2(self, init_variables_1870):
        assert init_variables_1870().min_speed_on_time(dist=[1, 3, 2], hour=1.9) == -1


"""
Test 1913. Maximum Product Difference Between Two Pairs
"""


@pytest.fixture(scope="session")
def init_variables_1913():
    from src.math_problems.maximum_product_difference_between_two_pairs import Solution

    solution = Solution()

    def _init_variables_1913():
        return solution

    yield _init_variables_1913


class TestClass1913:
    def test_solution_0(self, init_variables_1913):
        assert init_variables_1913().max_product_difference(nums=[5, 6, 2, 7, 4]) == 34

    def test_solution_1(self, init_variables_1913):
        assert (
            init_variables_1913().max_product_difference(nums=[4, 2, 5, 9, 7, 4, 8])
            == 64
        )


"""
Test 1922. Count Good Numbers
"""


@pytest.fixture(scope="session")
def init_variables_1922():
    from src.math_problems.count_good_numbers import Solution

    solution = Solution()

    def _init_variables_1922():
        return solution

    yield _init_variables_1922


class TestClass1922:
    def test_solution_0(self, init_variables_1922):
        assert init_variables_1922().count_good_numbers(n=1) == 5

    def test_solution_1(self, init_variables_1922):
        assert init_variables_1922().count_good_numbers(n=4) == 400

    def test_solution_2(self, init_variables_1922):
        assert init_variables_1922().count_good_numbers(n=50) == 564908303
