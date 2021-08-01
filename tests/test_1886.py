#!/usr/bin/env python

import pytest

"""
Test 1886. Determine Whether Matrix Can Be Obtained By Rotation
"""


@pytest.fixture(scope="session")
def init_variables_1886():
    from src.leetcode_1886_determine_whether_matrix_can_be_obtained_by_rotation import Solution

    solution = Solution()

    def _init_variables_1886():
        return solution

    yield _init_variables_1886


class TestClass1886:
    def test_solution_0(self, init_variables_1886):
        assert init_variables_1886().findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]])

    def test_solution_1(self, init_variables_1886):
        assert not init_variables_1886().findRotation(
            [[0, 1], [1, 1]], [[1, 0], [0, 1]]
        )

    def test_solution_2(self, init_variables_1886):
        assert init_variables_1886().findRotation(
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
        )
