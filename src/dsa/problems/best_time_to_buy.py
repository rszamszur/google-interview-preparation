"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/"""


def best_time_to_buy(prices):
    """Solved using Kadane algorithm.
    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        prices(List[int]): array prices where prices[i] is the price of a
            given stock on the ith day

    Returns:
        The maximum profit you can achieve from this transaction.
    """
    profit = 0
    buy = prices[0]

    for price in prices[1:]:
        if price <= buy:
            buy = price
            continue

        profit = max(profit, (price - buy))

    return profit
