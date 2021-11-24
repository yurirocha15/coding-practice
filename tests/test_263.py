#!/usr/bin/env python

import pytest

"""
Test 263. Ugly Number
"""


@pytest.fixture(scope="session")
def init_variables_263():
    from src.leetcode_263_ugly_number import Solution

    solution = Solution()

    def _init_variables_263():
        return solution

    yield _init_variables_263


class TestClass263:
    def test_solution_0(self, init_variables_263):
        assert init_variables_263().isUgly(6)

    def test_solution_1(self, init_variables_263):
        assert init_variables_263().isUgly(8)

    def test_solution_2(self, init_variables_263):
        assert not init_variables_263().isUgly(14)

    def test_solution_3(self, init_variables_263):
        assert init_variables_263().isUgly(1)
