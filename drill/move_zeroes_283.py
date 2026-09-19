"""
变式练习：LeetCode 283. 移动零（简单）
https://leetcode.cn/problems/move-zeroes/

题目：把所有 0 移到数组末尾，同时保持非零元素的相对顺序。
     必须原地操作，函数不返回任何东西。

为什么放这儿：这题就是 27 题的翻版，把"不等于 val"换成"不等于 0"。
            但多了一步——27 题不管尾巴，这题要把剩下的位置补成 0。
            先自己试，想清楚"哪些位置需要补 0、补几个"。
"""


def moveZeroes(nums):
    # 在这里写你的代码
    pass


if __name__ == "__main__":
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 0], [1, 0]),
        ([0, 0, 0], [0, 0, 0]),
    ]
    for nums, expected in cases:
        original = nums[:]
        moveZeroes(nums)
        ok = nums == expected
        print(f"[{'通过' if ok else '不通过'}] 输入 {original} → {nums}，期望 {expected}")