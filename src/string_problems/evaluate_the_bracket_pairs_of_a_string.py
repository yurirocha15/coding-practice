#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1807. Evaluate the Bracket Pairs of a String
URL: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/
"""
from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d_knowledge: DefaultDict[str, str] = defaultdict(
            lambda: "?", {a[0]: a[1] for a in knowledge}
        )
        key = ""
        start = -1
        ret = []
        for i, c in enumerate(s):
            if c == ")":
                key = s[start + 1 : i]
                ret.append(d_knowledge[key])
                start = -1
            elif c == "(":
                start = i
            elif start == -1:
                ret.append(c)
        return "".join(ret)


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.evaluate(
            s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]]
        )
        == "bobistwoyearsold"
    )
    assert solution.evaluate(s="hi(name)", knowledge=[["a", "b"]]) == "hi?"
    assert (
        solution.evaluate(s="(a)(a)(a)aaa", knowledge=[["a", "yes"]]) == "yesyesyesaaa"
    )
    assert solution.evaluate(s="(a)(b)", knowledge=[["a", "b"], ["b", "a"]]) == "ba"
