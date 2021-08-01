#!/usr/bin/env python

import pytest

"""
Test 1887. Reduction Operations to Make the Array Elements Equal
"""


@pytest.fixture(scope="session")
def init_variables_1887():
    from src.leetcode_1887_reduction_operations_to_make_the_array_elements_equal import Solution

    solution = Solution()

    def _init_variables_1887():
        return solution

    yield _init_variables_1887


class TestClass1887:
    def test_solution_0(self, init_variables_1887):
        assert init_variables_1887().reductionOperations([5, 1, 3]) == 3

    def test_solution_1(self, init_variables_1887):
        assert init_variables_1887().reductionOperations([1, 1, 1]) == 0

    def test_solution_2(self, init_variables_1887):
        assert init_variables_1887().reductionOperations([1, 1, 2, 2, 3]) == 4
