#!/usr/bin/env python

import pytest

"""
Test 1768. Merge Strings Alternately
"""


@pytest.fixture(scope="session")
def init_variables_1768():
    from src.leetcode_1768_merge_strings_alternately import Solution

    solution = Solution()

    def _init_variables_1768():
        return solution

    yield _init_variables_1768


class TestClass1768:
    def test_solution_0(self, init_variables_1768):
        assert init_variables_1768().mergeAlternately("abc", "pqr") == "apbqcr"

    def test_solution_1(self, init_variables_1768):
        assert init_variables_1768().mergeAlternately("ab", "pqrs") == "apbqrs"

    def test_solution_2(self, init_variables_1768):
        assert init_variables_1768().mergeAlternately("abcd", "pq") == "apbqcd"
