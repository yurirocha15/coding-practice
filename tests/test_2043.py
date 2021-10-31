#!/usr/bin/env python

import pytest

"""
Test 2043. Simple Bank System
"""


@pytest.fixture(scope="session")
def init_variables_2043():
    from src.leetcode_2043_simple_bank_system import Bank

    solution = Bank([10, 100, 20, 50, 30])

    def _init_variables_2043():
        return solution

    yield _init_variables_2043


class TestClass2043:
    def test_solution_0(self, init_variables_2043):
        assert init_variables_2043().withdraw(3, 10) == True
        assert init_variables_2043().transfer(5, 1, 20) == True
        assert init_variables_2043().deposit(5, 20) == True
        assert init_variables_2043().transfer(3, 4, 15) == False
        assert init_variables_2043().withdraw(10, 50) == False
