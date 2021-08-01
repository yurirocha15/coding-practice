#!/usr/bin/env python

import pytest

"""
Test 1897. Redistribute Characters to Make All Strings Equal
"""


@pytest.fixture(scope="session")
def init_variables_1897():
    from src.leetcode_1897_redistribute_characters_to_make_all_strings_equal import Solution

    solution = Solution()

    def _init_variables_1897():
        return solution

    yield _init_variables_1897


class TestClass1897:
    def test_solution_0(self, init_variables_1897):
        assert init_variables_1897().makeEqual(["abc", "aabc", "bc"])

    def test_solution_1(self, init_variables_1897):
        assert not init_variables_1897().makeEqual(["ab", "a"])
