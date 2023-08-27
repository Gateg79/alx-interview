#!/usr/bin/python3
''' Fewest number of coins needed to meet a given amount
from a given pile of coins of different values
'''

import math
# create makechange function


def makeChange(coins, total):
    if total <= 0:
        return 0
    cal = [math.inf] * (total+1)
    cal[0] = 0

    for coin in coins:
        for b in range(coin, total+1):
            if b-coin >= 0:
                cal[b] = min(cal[b], cal[b-coin]+1)

    return -1 if cal[-1] == math.inf else cal[-1]
