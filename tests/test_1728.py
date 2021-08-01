#!/usr/bin/env python

import pytest

"""
Test 1728. Cat and Mouse II
"""


@pytest.fixture(scope="session")
def init_variables_1728():
    from src.leetcode_1728_cat_and_mouse_ii import Solution

    solution = Solution()

    def _init_variables_1728():
        return solution

    yield _init_variables_1728


class TestClass1728:
    def test_solution_0(self, init_variables_1728):
        assert init_variables_1728().canMouseWin(["####F", "#C...", "M...."], 1, 2)

    def test_solution_1(self, init_variables_1728):
        assert init_variables_1728().canMouseWin(["M.C...F"], 1, 4)

    def test_solution_2(self, init_variables_1728):
        assert not init_variables_1728().canMouseWin(["M.C...F"], 1, 3)

    def test_solution_3(self, init_variables_1728):
        assert not init_variables_1728().canMouseWin(
            ["C...#", "...#F", "....#", "M...."], 2, 5
        )

    def test_solution_4(self, init_variables_1728):
        assert init_variables_1728().canMouseWin(
            [".M...", "..#..", "#..#.", "C#.#.", "...#F"], 3, 1
        )
