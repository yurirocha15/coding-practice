#!/usr/bin/env python

import pytest

"""
Test 1646. Get Maximum in Generated Array
"""


@pytest.fixture(scope="session")
def init_variables_1646():
    from src.leetcode_1646_get_maximum_in_generated_array import Solution

    solution = Solution()

    def _init_variables_1646():
        return solution

    yield _init_variables_1646


class TestClass1646:
    def test_solution_0(self, init_variables_1646):
        assert init_variables_1646().getMaximumGenerated(7) == 3

    def test_solution_1(self, init_variables_1646):
        assert init_variables_1646().getMaximumGenerated(2) == 1

    def test_solution_2(self, init_variables_1646):
        assert init_variables_1646().getMaximumGenerated(3) == 2
