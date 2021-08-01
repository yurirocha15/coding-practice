#!/usr/bin/env python

import pytest

"""
Test 1784. Check if Binary String Has at Most One Segment of Ones
"""


@pytest.fixture(scope="session")
def init_variables_1784():
    from src.leetcode_1784_check_if_binary_string_has_at_most_one_segment_of_ones import Solution

    solution = Solution()

    def _init_variables_1784():
        return solution

    yield _init_variables_1784


class TestClass1784:
    def test_solution_0(self, init_variables_1784):
        assert not init_variables_1784().checkOnesSegment("1001")

    def test_solution_1(self, init_variables_1784):
        assert init_variables_1784().checkOnesSegment("110")
