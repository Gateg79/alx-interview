#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    if total <= 0:
        return 0
    # The total no. of coins
    cal = [0] + [float("inf")] * (total)
    for coin in coins:
        for b in range(coin, total + 1):
            cal[b] = min(cal[b], cal[b - coin] + 1)
    # Return: fewest number of coins needed to meet total
    if cal[-1] != float("inf"):
        return cal[-1]
    return -1
