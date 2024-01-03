'''
In a realm where numbers hold secrets, 
a captivating challenge awaits, which is, Stock Buy and Sell Problem !!!

Our Task: The cost of a stock on each day is given in an array. 
Find the maximum profit that you can make by buying and selling on those days.
If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

Input: arr[] = {100, 180, 260, 310, 40, 535, 695}
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
                       Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
                       Maximum Profit  = 210 + 655 = 865
Input: arr[] = {4, 2, 2, 2, 4}
Output: 2
Explanation: Buy the stock on day 1 and sell it on day 4 => 4 – 2 = 2
                       Maximum Profit  = 2

'''


# naive approach for the problem
def naive_stock_selling(price,start,end):
    if end <= start:
        return 0
    profit = 0
    for i in range(start,end):
        for j in range(i+1,end+1):
            if price[j] > price[i]:
                currProfit = price[j] - price[i] + naive_stock_selling(price,start,i-1) + naive_stock_selling(price,j+1,end)
                profit = max(profit,currProfit)
                
    return profit

# efficient way
def stock_selling(price):
    n = len(price)
    profit = 0
    for i in range(1,n):
        if price[i] > price[i-1]:
            profit += price[i] - price[i-1]
    return profit
            
        
        


price = [100, 180, 260, 310, 40, 535, 695]
print(f"The Maximum profit of the stack is : {naive_stock_selling(price,0,len(price)-1)}")
print(f"The Maximum profit of the efficient stack is : {stock_selling(price)}")
        