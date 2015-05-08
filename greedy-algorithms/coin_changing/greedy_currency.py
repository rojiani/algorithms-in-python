"""
Coin Changing Problem - give change using fewest # of coins
Greedy Algorithm
Denominations: 1, 5, 10, 25, 100
"""

coin_values = [100, 25, 10, 5, 1]

def give_change(amount_due):
    coin_idx = 0
    coins = []
    while amount_due > 0:
        if amount_due >= coin_values[coin_idx]:
            amount_due -= coin_values[coin_idx]
            coins.append(coin_values[coin_idx])
        else:
            coin_idx += 1
    return coins


print(give_change(289))
