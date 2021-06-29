#!/usr/bin/env python

import pytest

"""
Test 1662: check_if_two_string_arrays_are_equivalent
"""


@pytest.fixture(scope="session")
def init_variables_1662():
    from src.string_problems.check_if_two_string_arrays_are_equivalent import Solution

    solution = Solution()

    def _init_variables_1662():
        return solution

    yield _init_variables_1662


class TestClass1662:
    def test_solution_0(self, init_variables_1662):
        assert init_variables_1662().array_strings_are_equal(["ab", "c"], ["a", "bc"])

    def test_solution_1(self, init_variables_1662):
        assert not init_variables_1662().array_strings_are_equal(
            ["a", "cb"], ["ab", "c"]
        )

    def test_solution_2(self, init_variables_1662):
        assert init_variables_1662().array_strings_are_equal(
            ["abc", "d", "defg"], ["abcddefg"]
        )


"""
Test 1657: determine_if_two_strings_are_close
"""


@pytest.fixture(scope="session")
def init_variables_1657():
    from src.string_problems.determine_if_two_strings_are_close import Solution

    solution = Solution()

    def _init_variables_1657():
        return solution

    yield _init_variables_1657


class TestClass1657:
    def test_solution_0(self, init_variables_1657):
        assert init_variables_1657().close_strings("abc", "bca")

    def test_solution_1(self, init_variables_1657):
        assert not init_variables_1657().close_strings("a", "aa")

    def test_solution_2(self, init_variables_1657):
        assert init_variables_1657().close_strings("cabbba", "abbccc")

    def test_solution_3(self, init_variables_1657):
        assert not init_variables_1657().close_strings("cabbba", "aabbss")


"""
Test 1663: smallest_string_with_a_given_numeric_value
"""


@pytest.fixture(scope="session")
def init_variables_1663():
    from src.string_problems.smallest_string_with_a_given_numeric_value import Solution

    solution = Solution()

    def _init_variables_1663():
        return solution

    yield _init_variables_1663


class TestClass1663:
    def test_solution_0(self, init_variables_1663):
        assert init_variables_1663().get_smallest_string(3, 27) == "aay"

    def test_solution_1(self, init_variables_1663):
        assert init_variables_1663().get_smallest_string(5, 73) == "aaszz"


"""
Test 1694. Reformat Phone Number
"""


@pytest.fixture(scope="session")
def init_variables_1694():
    from src.string_problems.reformat_phone_number import Solution

    solution = Solution()

    def _init_variables_1694():
        return solution

    yield _init_variables_1694


class TestClass1694:
    def test_solution_0(self, init_variables_1694):
        assert init_variables_1694().reformat_number("1-23-45 6") == "123-456"

    def test_solution_1(self, init_variables_1694):
        assert init_variables_1694().reformat_number("123 4-567") == "123-45-67"

    def test_solution_2(self, init_variables_1694):
        assert init_variables_1694().reformat_number("123 4-5678") == "123-456-78"

    def test_solution_3(self, init_variables_1694):
        assert init_variables_1694().reformat_number("12") == "12"

    def test_solution_4(self, init_variables_1694):
        assert (
            init_variables_1694().reformat_number("--17-5 229 35-39475 ")
            == "175-229-353-94-75"
        )


"""
Test 1736. Latest Time by Replacing Hidden Digits
"""


@pytest.fixture(scope="session")
def init_variables_1736():
    from src.string_problems.latest_time_by_replacing_hidden_digits import Solution

    solution = Solution()

    def _init_variables_1736():
        return solution

    yield _init_variables_1736


class TestClass1736:
    def test_solution_0(self, init_variables_1736):
        assert init_variables_1736().maximum_time("2?:?0") == "23:50"

    def test_solution_1(self, init_variables_1736):
        assert init_variables_1736().maximum_time("0?:3?") == "09:39"

    def test_solution_2(self, init_variables_1736):
        assert init_variables_1736().maximum_time("1?:22") == "19:22"


"""
Test 1737. Change Minimum Characters to Satisfy One of Three Conditions
"""


@pytest.fixture(scope="session")
def init_variables_1737():
    from src.string_problems.change_minimum_characters_to_satisfy_one_of_three_conditions import (
        Solution,
    )

    solution = Solution()

    def _init_variables_1737():
        return solution

    yield _init_variables_1737


class TestClass1737:
    def test_solution_0(self, init_variables_1737):
        assert init_variables_1737().min_characters(a="aba", b="caa") == 2

    def test_solution_1(self, init_variables_1737):
        assert init_variables_1737().min_characters(a="dabadd", b="cda") == 3


"""
Test 1759. Count Number of Homogenous Substrings
"""


@pytest.fixture(scope="session")
def init_variables_1759():
    from src.string_problems.count_number_of_homogenous_substrings import Solution

    solution = Solution()

    def _init_variables_1759():
        return solution

    yield _init_variables_1759


class TestClass1759:
    def test_solution_0(self, init_variables_1759):
        assert init_variables_1759().count_homogenous(s="abbcccaa") == 13

    def test_solution_1(self, init_variables_1759):
        assert init_variables_1759().count_homogenous(s="xy") == 2

    def test_solution_2(self, init_variables_1759):
        assert init_variables_1759().count_homogenous(s="zzzzz") == 15


"""
Test 1768. Merge Strings Alternately
"""


@pytest.fixture(scope="session")
def init_variables_1768():
    from src.string_problems.merge_strings_alternately import Solution

    solution = Solution()

    def _init_variables_1768():
        return solution

    yield _init_variables_1768


class TestClass1768:
    def test_solution_0(self, init_variables_1768):
        assert (
            init_variables_1768().merge_alternately(word1="abc", word2="pqr")
            == "apbqcr"
        )

    def test_solution_1(self, init_variables_1768):
        assert (
            init_variables_1768().merge_alternately(word1="ab", word2="pqrs")
            == "apbqrs"
        )

    def test_solution_2(self, init_variables_1768):
        assert (
            init_variables_1768().merge_alternately(word1="abcd", word2="pq")
            == "apbqcd"
        )


"""
Test 1790. Check if One String Swap Can Make Strings Equal
"""


@pytest.fixture(scope="session")
def init_variables_1790():
    from src.string_problems.check_if_one_string_swap_can_make_strings_equal import Solution

    solution = Solution()

    def _init_variables_1790():
        return solution

    yield _init_variables_1790


class TestClass1790:
    def test_solution_0(self, init_variables_1790):
        assert init_variables_1790().are_almost_equal(s1="bank", s2="kanb")

    def test_solution_1(self, init_variables_1790):
        assert not init_variables_1790().are_almost_equal(s1="attack", s2="defend")

    def test_solution_2(self, init_variables_1790):
        assert init_variables_1790().are_almost_equal(s1="kelb", s2="kelb")

    def test_solution_3(self, init_variables_1790):
        assert not init_variables_1790().are_almost_equal(s1="abcd", s2="dcba")


"""
Test 1805. Number of Different Integers in a String
"""


@pytest.fixture(scope="session")
def init_variables_1805():
    from src.string_problems.number_of_different_integers_in_a_string import Solution

    solution = Solution()

    def _init_variables_1805():
        return solution

    yield _init_variables_1805


class TestClass1805:
    def test_solution_0(self, init_variables_1805):
        assert init_variables_1805().num_different_integers(word="a123bc34d8ef34") == 3

    def test_solution_1(self, init_variables_1805):
        assert init_variables_1805().num_different_integers(word="leet1234code234") == 2

    def test_solution_2(self, init_variables_1805):
        assert init_variables_1805().num_different_integers(word="a1b01c001") == 1


"""
Test 1807. Evaluate the Bracket Pairs of a String
"""


@pytest.fixture(scope="session")
def init_variables_1807():
    from src.string_problems.evaluate_the_bracket_pairs_of_a_string import Solution

    solution = Solution()

    def _init_variables_1807():
        return solution

    yield _init_variables_1807


class TestClass1807:
    def test_solution_0(self, init_variables_1807):
        assert (
            init_variables_1807().evaluate(
                s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]
            )
            == "bobistwoyearsold"
        )

    def test_solution_1(self, init_variables_1807):
        assert (
            init_variables_1807().evaluate(s="hi(name)", knowledge=[["a", "b"]])
            == "hi?"
        )

    def test_solution_2(self, init_variables_1807):
        assert (
            init_variables_1807().evaluate(s="(a)(a)(a)aaa", knowledge=[["a", "yes"]])
            == "yesyesyesaaa"
        )

    def test_solution_3(self, init_variables_1807):
        assert (
            init_variables_1807().evaluate(
                s="(a)(b)", knowledge=[["a", "b"], ["b", "a"]]
            )
            == "ba"
        )


"""
Test 1832. Check if the Sentence Is Pangram
"""


@pytest.fixture(scope="session")
def init_variables_1832():
    from src.string_problems.check_if_the_sentence_is_pangram import Solution

    solution = Solution()

    def _init_variables_1832():
        return solution

    yield _init_variables_1832


class TestClass1832:
    def test_solution_0(self, init_variables_1832):
        assert init_variables_1832().check_if_pangram(
            sentence="thequickbrownfoxjumpsoverthelazydog"
        )

    def test_solution_1(self, init_variables_1832):
        assert not init_variables_1832().check_if_pangram(sentence="leetcode")


"""
Test 1839. Longest Substring Of All Vowels in Order
"""


@pytest.fixture(scope="session")
def init_variables_1839():
    from src.string_problems.longest_substring_of_all_vowels_in_order import Solution

    solution = Solution()

    def _init_variables_1839():
        return solution

    yield _init_variables_1839


class TestClass1839:
    def test_solution_0(self, init_variables_1839):
        assert (
            init_variables_1839().longest_beautiful_substring(
                word="aeiaaioaaaaeiiiiouuuooaauuaeiu"
            )
            == 13
        )

    def test_solution_1(self, init_variables_1839):
        assert (
            init_variables_1839().longest_beautiful_substring(
                word="aeeeiiiioooauuuaeiou"
            )
            == 5
        )

    def test_solution_2(self, init_variables_1839):
        assert init_variables_1839().longest_beautiful_substring(word="a") == 0


"""
Test 1880. Check if Word Equals Summation of Two Words
"""


@pytest.fixture(scope="session")
def init_variables_1880():
    from src.string_problems.check_if_word_equals_summation_of_two_words import Solution

    solution = Solution()

    def _init_variables_1880():
        return solution

    yield _init_variables_1880


class TestClass1880:
    def test_solution_0(self, init_variables_1880):
        assert init_variables_1880().is_sum_equal(
            firstWord="acb", secondWord="cba", targetWord="cdb"
        )

    def test_solution_1(self, init_variables_1880):
        assert not init_variables_1880().is_sum_equal(
            firstWord="aaa", secondWord="a", targetWord="aab"
        )

    def test_solution_2(self, init_variables_1880):
        assert init_variables_1880().is_sum_equal(
            firstWord="aaa", secondWord="a", targetWord="aaaa"
        )


"""
Test 1897. Redistribute Characters to Make All Strings Equal
"""


@pytest.fixture(scope="session")
def init_variables_1897():
    from src.string_problems.redistribute_characters_to_make_all_strings_equal import Solution

    solution = Solution()

    def _init_variables_1897():
        return solution

    yield _init_variables_1897


class TestClass1897:
    def test_solution_0(self, init_variables_1897):
        assert init_variables_1897().make_equal(words=["abc", "aabc", "bc"])

    def test_solution_1(self, init_variables_1897):
        assert not init_variables_1897().make_equal(words=["ab", "a"])
