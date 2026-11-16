def best_time_toBuy_stock(prices):
    max = 0
    for i in range(1, len(prices)):
        profit = prices[i] - prices[i - 1]
        if profit > 0:
            max += profit

    return max

print(best_time_toBuy_stock([7,1,5,3,6,4]))
