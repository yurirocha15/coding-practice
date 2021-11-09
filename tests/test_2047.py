#!/usr/bin/env python

import pytest

"""
Test 2047. Number of Valid Words in a Sentence
"""


@pytest.fixture(scope="session")
def init_variables_2047():
    from src.leetcode_2047_number_of_valid_words_in_a_sentence import Solution

    solution = Solution()

    def _init_variables_2047():
        return solution

    yield _init_variables_2047


class TestClass2047:
    def test_solution_0(self, init_variables_2047):
        assert init_variables_2047().countValidWords("cat and  dog") == 3

    def test_solution_1(self, init_variables_2047):
        assert init_variables_2047().countValidWords("!this  1-s b8d!") == 0

    def test_solution_2(self, init_variables_2047):
        assert (
            init_variables_2047().countValidWords(
                "alice and  bob are playing stone-game10"
            )
            == 5
        )

    def test_solution_3(self, init_variables_2047):
        assert (
            init_variables_2047().countValidWords(
                "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
            )
            == 6
        )

    def test_solution_4(self, init_variables_2047):
        assert (
            init_variables_2047().countValidWords(
                " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
            )
            == 49
        )
