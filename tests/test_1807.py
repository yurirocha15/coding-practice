#!/usr/bin/env python

import pytest

"""
Test 1807. Evaluate the Bracket Pairs of a String
"""


@pytest.fixture(scope="session")
def init_variables_1807():
    from src.leetcode_1807_evaluate_the_bracket_pairs_of_a_string import Solution

    solution = Solution()

    def _init_variables_1807():
        return solution

    yield _init_variables_1807


class TestClass1807:
    def test_solution_0(self, init_variables_1807):
        assert (
            init_variables_1807().evaluate(
                "(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]
            )
            == "bobistwoyearsold"
        )

    def test_solution_1(self, init_variables_1807):
        assert init_variables_1807().evaluate("hi(name)", [["a", "b"]]) == "hi?"

    def test_solution_2(self, init_variables_1807):
        assert (
            init_variables_1807().evaluate("(a)(a)(a)aaa", [["a", "yes"]])
            == "yesyesyesaaa"
        )

    def test_solution_3(self, init_variables_1807):
        assert (
            init_variables_1807().evaluate("(a)(b)", [["a", "b"], ["b", "a"]]) == "ba"
        )
