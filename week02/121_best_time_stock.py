"""
LeetCode 121. 买卖股票的最佳时机（简单）
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

题目：prices[i] 表示第 i 天的股票价格。
      你只能选一天买入、在之后某一天卖出，最多完成一笔交易。
      返回能获得的最大利润；如果怎么都赚不到钱，返回 0。

思路：
1. 手上记两个数：最低价格、最大利润
2. 每走到一天，先算当天卖出的利润，比最大利润大就更新
3. 如果今天比最低价还低，就把最低价换掉
4. 只需要扫一遍，因为最低价和最大利润在走的过程中就全部攒出来了，第二遍没有新信息可用


复杂度：时间 O(n)，空间 O(1)

提示：只需要遍历一遍。一边走一边记住「到目前为止见过的最低价格」，
      每到一天就算一下「如果今天卖，能赚多少」= 今天价格 - 历史最低价，
      把赚得最多的那次记下来。
      注意：价格一路下跌时，不买才是最优，答案是 0，别让负数赢。
"""


def maxProfit(prices):
    min_price = prices[0]
    profit = 0
    for x in prices:
        if x-min_price > profit:
            profit = x-min_price
        if x < min_price:
            min_price = x
    return profit




if __name__ == "__main__":
    cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
    ]
    for prices, expected in cases:
        result = maxProfit(prices)
        ok = result == expected
        print(f"[{'通过' if ok else '不通过'}] {prices} -> {result}，期望 {expected}")
