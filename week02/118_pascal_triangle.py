"""
LeetCode 118. 杨辉三角（简单）
https://leetcode.cn/problems/pascals-triangle/

题目：给定行数 numRows，返回杨辉三角的前 numRows 行。

规律（三句话）
    1. 第 i 行有 i + 1 个数字
    2. 每行的第一个和最后一个永远是 1
    3. 中间的数 = 上一行相邻两个数之和
       也就是：第 i 行第 j 个 = 上一行[j-1] + 上一行[j]   （1 <= j <= i-1）

思路：一行一行地造。
      循环走到第 i 行时，result 里已经存好了第 0 ~ i-1 行，
      所以「上一行」就是 result[i - 1]。
      先造一个全 1 的 row 当底子，再把中间几个位置改成上一行相邻两数之和。

复杂度：时间 O(numRows²)，空间 O(numRows²)（答案本身）

易错点：
    1. 数据源必须是「上一行 result[i-1]」，不能是「当前行 row」。
       一个变量不能同时当输入和输出：row 是要被填的答案，
       它既不包含上一行的数据，又会在填充过程中被逐步改写，越算越偏。
    2. i = 0 和 i = 1 时 range(1, i) 是空的，循环体一次都不执行，
       这正好对应「前两行没有中间元素」，所以不用写特殊判断。
"""


def generate(numRows):
    result = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


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