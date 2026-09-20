"""
LeetCode 118. 杨辉三角（简单）
https://leetcode.cn/problems/pascals-triangle/

题目：给定行数 numRows，返回杨辉三角的前 numRows 行。

例如 numRows = 5，返回：
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]

思路：（先用中文把你的想法写在这里）


复杂度：时间 O(numRows²)，空间 O(numRows²)（答案本身）

提示：每一行的第一个和最后一个永远是 1。
      中间的元素 = 上一行的「同一位置」+ 上一行的「前一个位置」。
      例如第 4 行的 6 = 第 3 行的 3 + 第 3 行的 3。
      可以一行一行地造，每次用上一行的数据算出这一行。
"""


def generate(numRows):
    # TODO: 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        (2, [[1], [1, 1]]),
    ]
    for numRows, expected in cases:
        result = generate(numRows)
        ok = result == expected
        print(f"[{'通过' if ok else '不通过'}] numRows={numRows} -> {result}")