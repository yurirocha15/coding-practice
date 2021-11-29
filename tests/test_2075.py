#!/usr/bin/env python

import pytest

"""
Test 2075. Decode the Slanted Ciphertext
"""


@pytest.fixture(scope="session")
def init_variables_2075():
    from src.leetcode_2075_decode_the_slanted_ciphertext import Solution

    solution = Solution()

    def _init_variables_2075():
        return solution

    yield _init_variables_2075


class TestClass2075:
    def test_solution_0(self, init_variables_2075):
        assert init_variables_2075().decodeCiphertext("ch   ie   pr", 3) == "cipher"

    def test_solution_1(self, init_variables_2075):
        assert (
            init_variables_2075().decodeCiphertext("iveo    eed   l te   olc", 4)
            == "i love leetcode"
        )

    def test_solution_2(self, init_variables_2075):
        assert init_variables_2075().decodeCiphertext("coding", 1) == "coding"

    def test_solution_3(self, init_variables_2075):
        assert init_variables_2075().decodeCiphertext(" b  ac", 2) == " abc"
