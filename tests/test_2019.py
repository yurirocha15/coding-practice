#!/usr/bin/env python

import pytest

"""
Test 2019. The Score of Students Solving Math Expression
"""


@pytest.fixture(scope="session")
def init_variables_2019():
    from src.leetcode_2019_the_score_of_students_solving_math_expression import Solution

    solution = Solution()

    def _init_variables_2019():
        return solution

    yield _init_variables_2019


class TestClass2019:
    def test_solution_0(self, init_variables_2019):
        assert init_variables_2019().scoreOfStudents("7+3*1*2", [20, 13, 42]) == 7

    def test_solution_1(self, init_variables_2019):
        assert (
            init_variables_2019().scoreOfStudents("3+5*2", [13, 0, 10, 13, 13, 16, 16])
            == 19
        )

    def test_solution_2(self, init_variables_2019):
        assert init_variables_2019().scoreOfStudents("6+0*1", [12, 9, 6, 4, 8, 6]) == 10

    def test_solution_3(self, init_variables_2019):
        assert init_variables_2019().scoreOfStudents("1+2*3+4", [13, 21, 11, 15]) == 11
