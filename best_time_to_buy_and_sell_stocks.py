def maxProfit(prices):
    if len(prices) < 2:
        return 0
    left = 0 #Buy
    right = 1 #Sell
    max_profit = 0
    to_buy = [0, 0]
    while right < len(prices):
        currentProfit = prices[right] - prices[left] #our current Profit
        if prices[left] < prices[right]:
            if currentProfit > max_profit:
                max_profit = currentProfit
                to_buy = [left, right]
        else:
            left = right
        right += 1
    return max_profit, to_buy



print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))