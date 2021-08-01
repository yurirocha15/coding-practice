#!/usr/bin/env python

import pytest

"""
Test 1837. Sum of Digits in Base K
"""


@pytest.fixture(scope="session")
def init_variables_1837():
    from src.leetcode_1837_sum_of_digits_in_base_k import Solution

    solution = Solution()

    def _init_variables_1837():
        return solution

    yield _init_variables_1837


class TestClass1837:
    def test_solution_0(self, init_variables_1837):
        assert init_variables_1837().sumBase(34, 6) == 9

    def test_solution_1(self, init_variables_1837):
        assert init_variables_1837().sumBase(10, 10) == 1
