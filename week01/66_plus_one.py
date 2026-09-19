"""
LeetCode 66. 加一（简单）
https://leetcode.cn/problems/plus-one/

题目：给定一个由整数组成的非空数组 digits 表示一个非负整数，
      在该数的基础上加一，返回结果数组。

思路：把数组当成十进制数，加一从最低位（数组最后一位）开始处理。
      倒着遍历每一位：
        - 这一位小于 9 → 加一，然后立刻 return（不会再有进位了）
        - 这一位等于 9 → 变成 0，继续往前看（把进位传给前一位）
      如果整个数组都是 9，循环会完整走完，每一位都被改成 0，
      这时在最前面补一个 1，数组长度会加一。

复杂度：时间 O(n)（最坏情况扫一遍），空间 O(1)

易错点：
      1. 判断的是 digits[i]（位置上的值），不是 i（下标）
      2. 倒着遍历时 range 的终点必须写 -1，否则走不到下标 0
      3. 赋值用 =，不是 ==
"""


def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits


if __name__ == "__main__":
    cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),
    ]
    for digits, expected in cases:
        original = digits[:]
        result = plusOne(digits)
        ok = result == expected
        print(f"[{'通过' if ok else '不通过'}] 输入 {original} → {result}，期望 {expected}")