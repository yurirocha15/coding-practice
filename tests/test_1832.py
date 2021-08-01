#!/usr/bin/env python

import pytest

"""
Test 1832. Check if the Sentence Is Pangram
"""


@pytest.fixture(scope="session")
def init_variables_1832():
    from src.leetcode_1832_check_if_the_sentence_is_pangram import Solution

    solution = Solution()

    def _init_variables_1832():
        return solution

    yield _init_variables_1832


class TestClass1832:
    def test_solution_0(self, init_variables_1832):
        assert init_variables_1832().checkIfPangram(
            "thequickbrownfoxjumpsoverthelazydog"
        )

    def test_solution_1(self, init_variables_1832):
        assert not init_variables_1832().checkIfPangram("leetcode")
