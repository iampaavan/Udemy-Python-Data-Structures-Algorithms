def coin_change(target, coins, known_result):

    # Default min_coins to target
    min_coins = target

    # Check if there is a single coin match
    if target in coins:
        known_result[target] = 1
        return 1

    # Return if known_result if it happens to be greater than 1
    elif known_result[target] > 0:
        return known_result[target]

    else:

        # for every coin value that is less than or equal to the target
        for i in [coin for coin in coins if coin <= target]:

            # Recursive Call, add a coin and subtract from the target
            num_of_coins = 1 + coin_change(target-i, coins, known_result)

            # Reset the minimum if we have a new minimum
            if num_of_coins < min_coins:
                min_coins = num_of_coins

                # Reset the known_result
                known_result[target] = min_coins

    return min_coins


# target = 63
# coins = [1, 5, 10, 25]
# known_target = [0] * (target+1)
# print(coin_change(target, coins, known_target))
print(coin_change(74, [1, 5, 10, 25], known_result=[0]*(74+1)))
