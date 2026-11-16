def best_time_to_buy_sell_stock(prices):
    min = prices[0]
    maxProfit = 0

    for i in range(len(prices)):
        if prices[i] - min > maxProfit:
            maxProfit = prices[i] - min

        if min > prices[i]:
            min = prices[i]

    return maxProfit

print(best_time_to_buy_sell_stock([7,1,5,3,6,4]))
