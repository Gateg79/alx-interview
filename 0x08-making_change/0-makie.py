#!/usr/bin/python3
""" Determines the minimum number of coins required to get total """

def makeChange(coins, total):
    """ Find total number of coins required to get total"""
    num_of_coins = 0
    if total <= 0:
        return 0
    # checking for empty coins
    if not coins:
        return -1
    coins = sorted(coins)
    first_big = len(coins) - 1
    # Checking if the mimimum coin we have is
    # greater than total (coins is sorted)
    # In that case total cannot be achieved
    if (coins[0] > total):
        return -1
    adj_total = total
    while ((adj_total) != 0 and first_big >= 0):
        if coins[first_big] > adj_total:
            first_big -= 1
        else:
            num_of_coins += (adj_total // coins[first_big])
            adj_total = adj_total % coins[first_big]
            first_big -= 1
    # This check is required because the loop might have
    # exited due to first_big being less than 0 (meaning
    # its impossible to achieve total with the coins we have)
    if (adj_total == 0):
        return num_of_coins
    return -1
