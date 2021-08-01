#!/usr/bin/env python

import pytest

"""
Test 1913. Maximum Product Difference Between Two Pairs
"""


@pytest.fixture(scope="session")
def init_variables_1913():
    from src.leetcode_1913_maximum_product_difference_between_two_pairs import Solution

    solution = Solution()

    def _init_variables_1913():
        return solution

    yield _init_variables_1913


class TestClass1913:
    def test_solution_0(self, init_variables_1913):
        assert init_variables_1913().maxProductDifference([5, 6, 2, 7, 4]) == 34

    def test_solution_1(self, init_variables_1913):
        assert init_variables_1913().maxProductDifference([4, 2, 5, 9, 7, 4, 8]) == 64
