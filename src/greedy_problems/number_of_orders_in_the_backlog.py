#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1801. Number of Orders in the Backlog
URL: https://leetcode.com/problems/number-of-orders-in-the-backlog/description/
"""
import heapq
from typing import List, Tuple


class Solution:
    def get_number_of_backlog_orders(self, orders: List[List[int]]) -> int:
        buy_pq: List[Tuple[int, int]] = []
        sell_pq: List[Tuple[int, int]] = []
        for order in orders:
            # sell
            if order[-1]:
                sell = order
                while buy_pq and (-buy_pq[0][0]) >= sell[0] and sell[1] > 0:
                    buy_v, buy_a = heapq.heappop(buy_pq)
                    if buy_a <= sell[1]:
                        sell[1] -= buy_a
                    else:
                        buy_a -= sell[1]
                        sell[1] = 0
                        heapq.heappush(buy_pq, (buy_v, buy_a))

                if sell[1]:
                    heapq.heappush(sell_pq, (sell[0], sell[1]))
            # buy
            else:
                buy = order
                while sell_pq and sell_pq[0][0] <= buy[0] and buy[1] > 0:
                    sell_v, sell_a = heapq.heappop(sell_pq)
                    if sell_a <= buy[1]:
                        buy[1] -= sell_a
                    else:
                        sell_a -= buy[1]
                        buy[1] = 0
                        heapq.heappush(sell_pq, (sell_v, sell_a))

                if buy[1]:
                    heapq.heappush(buy_pq, (-buy[0], buy[1]))
        return (
            sum(map(lambda b: b[1], buy_pq)) + sum(map(lambda s: s[1], sell_pq))
        ) % (10 ** 9 + 7)


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.get_number_of_backlog_orders(
            orders=[[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
        )
        == 6
    )
    assert (
        solution.get_number_of_backlog_orders(
            orders=[[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
        )
        == 999999984
    )
