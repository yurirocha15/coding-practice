#!/usr/bin/env python

import pytest

"""
Test 1739. Building Boxes
"""


@pytest.fixture(scope="session")
def init_variables_1739():
    from src.leetcode_1739_building_boxes import Solution

    solution = Solution()

    def _init_variables_1739():
        return solution

    yield _init_variables_1739


class TestClass1739:
    def test_solution_0(self, init_variables_1739):
        assert init_variables_1739().minimumBoxes(3) == 3

    def test_solution_1(self, init_variables_1739):
        assert init_variables_1739().minimumBoxes(4) == 3

    def test_solution_2(self, init_variables_1739):
        assert init_variables_1739().minimumBoxes(10) == 6
