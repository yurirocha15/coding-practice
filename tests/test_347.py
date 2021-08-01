#!/usr/bin/env python

import pytest

"""
Test 347. Top K Frequent Elements
"""


@pytest.fixture(scope="session")
def init_variables_347():
    from src.leetcode_347_top_k_frequent_elements import Solution

    solution = Solution()

    def _init_variables_347():
        return solution

    yield _init_variables_347


class TestClass347:
    def test_solution_0(self, init_variables_347):
        assert init_variables_347().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]

    def test_solution_1(self, init_variables_347):
        assert init_variables_347().topKFrequent([1], 1) == [1]
