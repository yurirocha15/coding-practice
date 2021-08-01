#!/usr/bin/env python

import pytest

"""
Test 1871. Jump Game VII
"""


@pytest.fixture(scope="session")
def init_variables_1871():
    from src.leetcode_1871_jump_game_vii import Solution

    solution = Solution()

    def _init_variables_1871():
        return solution

    yield _init_variables_1871


class TestClass1871:
    def test_solution_0(self, init_variables_1871):
        assert init_variables_1871().canReach("011010", 2, 3)

    def test_solution_1(self, init_variables_1871):
        assert not init_variables_1871().canReach("01101110", 2, 3)
