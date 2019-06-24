def coin_change(target, list_of_coins):

    # Default to target value
    min_coins = target

    # Check to see if we have a single coin match (Base Case)
    if target in list_of_coins:
        return 1

    else:

        # for every coin value that is <= target
        for i in [coins for coins in list_of_coins if coins <= target]:

            # Recursive Call (add a coin and subtract from the target)
            num_of_coins = 1 + coin_change(target - i, list_of_coins)

            # Reset Minimum if we have a new minimum
            if num_of_coins < min_coins:
                min_coins = num_of_coins

    return min_coins


print(coin_change(15, [1, 2, 5, 10]))
print(coin_change(63, [1, 5, 10, 25]))
