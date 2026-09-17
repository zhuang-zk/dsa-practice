"""
LeetCode 66. 加一（简单）
https://leetcode.cn/problems/plus-one/

题目：给定一个由整数组成的非空数组 digits 表示一个非负整数，
      在该数的基础上加一，返回结果数组。

思路：（先用中文把你的想法写在这里）


复杂度：时间 O(n)，空间 O(1)（不算返回值）

提示：从最后一位往前处理。只加 1，所以最多产生一次进位。
      最麻烦的是 999 这种全是 9 的情况，答案是 1000，数组长度会变。
"""


def plusOne(digits):
    # TODO: 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
    ]
    for digits, expected in cases:
        result = plusOne(digits)
        ok = result == expected
        print(f"[{'通过' if ok else '不通过'}] 输入 {digits} → {result}，期望 {expected}")