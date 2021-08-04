#!/usr/bin/env python

import pytest

"""
Test 1656. Design an Ordered Stream
"""


@pytest.fixture(scope="session")
def init_variables_1656():
    from src.leetcode_1656_design_an_ordered_stream import OrderedStream

    solution = OrderedStream(5)

    def _init_variables_1656():
        return solution

    yield _init_variables_1656


class TestClass1656:
    def test_solution_0(self, init_variables_1656):
        assert init_variables_1656().insert(3, "ccccc") == []
        assert init_variables_1656().insert(1, "aaaaa") == ["aaaaa"]
        assert init_variables_1656().insert(2, "bbbbb") == ["bbbbb", "ccccc"]
        assert init_variables_1656().insert(5, "eeeee") == []
        assert init_variables_1656().insert(4, "ddddd") == ["ddddd", "eeeee"]
