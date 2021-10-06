#!/usr/bin/env python

import pytest

"""
Test 2013. Detect Squares
"""


@pytest.fixture(scope="session")
def init_variables_2013():
    from src.leetcode_2013_detect_squares import DetectSquares

    solution = DetectSquares()

    def _init_variables_2013():
        return solution

    yield _init_variables_2013


class TestClass2013:
    def test_solution_0(self, init_variables_2013):
        assert init_variables_2013().add([3, 10]) == None
        assert init_variables_2013().add([11, 2]) == None
        assert init_variables_2013().add([3, 2]) == None
        assert init_variables_2013().count([11, 10]) == 1
        assert init_variables_2013().count([14, 8]) == 0
        assert init_variables_2013().add([11, 2]) == None
        assert init_variables_2013().count([11, 10]) == 2
