class SellStock:
    def sell_stock(self, list):
        max_sell_price = list[-1]
        max_profit = 0
        if len(list) <= 1:
            return 0
        for i in range(len(list)-2, -1, -1):
            if list[i] > max_sell_price:
                max_sell_price = list[i]
            profit = max_sell_price - list[i]
            max_profit = max(max_profit, profit)
        return max_profit


prices = [7, 6, 4, 3, 1]
a = SellStock()
print(a.sell_stock(prices))
