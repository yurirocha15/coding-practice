#!/usr/bin/env python

import pytest

"""
Test 1869. Longer Contiguous Segments of Ones than Zeros
"""


@pytest.fixture(scope="session")
def init_variables_1869():
    from src.leetcode_1869_longer_contiguous_segments_of_ones_than_zeros import Solution

    solution = Solution()

    def _init_variables_1869():
        return solution

    yield _init_variables_1869


class TestClass1869:
    def test_solution_0(self, init_variables_1869):
        assert init_variables_1869().checkZeroOnes("1101")

    def test_solution_1(self, init_variables_1869):
        assert not init_variables_1869().checkZeroOnes("111000")

    def test_solution_2(self, init_variables_1869):
        assert not init_variables_1869().checkZeroOnes("110100010")
